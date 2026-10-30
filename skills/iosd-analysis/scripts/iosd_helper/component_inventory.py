"""Offline metadata facets for architecture/protocol triage; no inferred ownership."""
from collections import Counter,defaultdict
from copy import deepcopy
import re


def _rva(value):
    if value is None:return None
    if isinstance(value,bool):raise ValueError('Boolean is not an RVA')
    parsed=int(value,0) if isinstance(value,str) else value
    if not isinstance(parsed,int) or not 0 <= parsed < 1<<64:raise ValueError('Invalid image RVA')
    return parsed


def build_component_inventory(model, expected_md5=None, query=None, category=None, match='token'):
    """Index every source row, including duplicate names and incomplete records.

    Filtering selects IDs without removing entities or unknowns. Name tokens are
    lexical facets; they neither classify network protocols nor create hierarchy.
    """
    if model.get('kind') not in ('protocol_subsystem_index','iosd_architecture_map') or model.get('address_space')!='rva':
        raise ValueError('Expected a saved RVA subsystem index or architecture map')
    raw_md5=model.get('input_md5');md5=raw_md5.strip() if isinstance(raw_md5,str) and raw_md5.strip() else None
    if expected_md5 and (not md5 or md5.lower()!=expected_md5.lower()):
        raise ValueError('Component index input MD5 mismatch')
    if match not in ('token','contains'):raise ValueError('Choose token or contains matching')
    query=query.strip().casefold() if query else None
    category=category.strip().casefold() if category else None
    entities=[];selected=[];unknown=[];by_category=defaultdict(list);by_token=defaultdict(list)
    if md5 is None:unknown.append({'reason':'source_input_identity_not_recorded','raw_value':deepcopy(raw_md5)})
    by_name=defaultdict(list);by_init=defaultdict(list);record_counts=Counter()
    for index,source in enumerate(model['subsystems']):
        if not isinstance(source,dict):raise ValueError('Subsystem records must be JSON objects')
        gaps=[];addresses={}
        for key in ('record_rva','init_rva'):
            try:addresses[key]=_rva(source.get(key))
            except (ValueError,TypeError):
                addresses[key]=None;gaps.append({'reason':'invalid_'+key,'raw_value':deepcopy(source.get(key))})
            else:
                if addresses[key] is None:gaps.append({'reason':key+'_not_recorded'})
        rva=addresses['record_rva'];prefix='subsystem:%X'%rva if rva is not None else 'subsystem:unlocated:%d'%index
        occurrence=record_counts[prefix];record_counts[prefix]+=1
        entity_id=prefix+(':%d'%occurrence if occurrence else '')
        if occurrence:gaps.append({'reason':'duplicate_record_rva','earlier_id':prefix})
        name=source.get('name') if isinstance(source.get('name'),str) and source['name'].strip() else None
        label=source.get('category') if isinstance(source.get('category'),str) and source['category'].strip() else 'unknown'
        if name is None:gaps.append({'reason':'name_not_recorded'})
        if label=='unknown':gaps.append({'reason':'category_unreviewed'})
        tokens=sorted(set(re.findall(r'[a-z0-9]+',name.casefold()))) if name else []
        row={'id':entity_id,'name':name,'category':label,**addresses,'name_tokens':tokens,
             'source_row_index':index,'source_record':deepcopy(source),'gaps':gaps,
             'packet_role':'unverified','runtime_activation':'unobserved','implementation_owner':'unresolved'}
        entities.append(row);by_category[label].append(entity_id)
        for token in tokens:by_token[token].append(entity_id)
        if name:by_name[name].append(entity_id)
        if addresses['init_rva'] is not None:by_init[addresses['init_rva']].append(entity_id)
        for gap in gaps:unknown.append({'entity_id':entity_id,**gap})
        name_matches = query is None or (query in tokens if match=='token' else name is not None and query in name.casefold())
        if name_matches and (category is None or label.casefold()==category):selected.append(entity_id)
    duplicate_names=[{'name':name,'entity_ids':ids,'relation':'same_name_only; semantic equivalence unresolved'}
                     for name,ids in sorted(by_name.items()) if len(ids)>1]
    shared_init=[{'init_rva':rva,'entity_ids':ids,'relation':'shared_recorded_init_only; ownership unresolved'}
                 for rva,ids in sorted(by_init.items()) if len(ids)>1]
    return {'schema_version':1,'kind':'iosd_component_inventory','input_md5':md5,'address_space':'rva',
            'source':'saved_subsystem_metadata','current_idb_verified':False,
            'selection':{'query':query,'category':category,'match':match,'entity_ids':selected},
            'summary':{'source_records':len(entities),'selected_records':len(selected),'distinct_names':len(by_name),
                       'categories':len(by_category),'lexical_tokens':len(by_token),'records_with_gaps':sum(bool(r['gaps']) for r in entities),
                       'unknown_items':len(unknown),'duplicate_name_groups':len(duplicate_names),'shared_init_groups':len(shared_init)},
            'facets':{'categories':[{'name':name,'count':len(ids),'entity_ids':ids} for name,ids in sorted(by_category.items())],
                      'name_tokens':[{'token':token,'count':len(ids),'entity_ids':ids} for token,ids in sorted(by_token.items())]},
            'entities':entities,'duplicate_names':duplicate_names,'shared_init':shared_init,'unknown':unknown,
            'limits':['Name tokens and categories are search facets, not verified network protocols or a component hierarchy.',
                      'Same names or init RVAs do not prove containment, semantic equivalence or current execution.',
                      'All source rows and gaps are retained; selection only chooses IDs.',
                      'A historical metadata index is not a fresh IDB or runtime capture.']}
