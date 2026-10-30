"""Trace acquired terminal cohorts through mode roots and conditional registration edges."""
from collections import defaultdict,deque,Counter
from .syntax_paths import semantic_options,raw_links


REFERENCE_FIELDS={'node','source','target','function','variable_address','function_candidate','callback',
    'source_address','decoder_address','predicate_candidate','false_target_candidate','bounds_callback','validation_callback'}


def reference_va(ref,base):
    if not ref:return 0
    return base+ref['rva'] if ref['space']=='image' else ref['va']


def restore_value(value,base):
    if isinstance(value,list):return [restore_value(x,base) for x in value]
    if not isinstance(value,dict):return value
    out={}
    for name,item in value.items():
        if name.endswith('_rva') and name[:-4] in REFERENCE_FIELDS:out[name[:-4]]=base+item
        elif name.endswith('_captured_va') and name[:-12] in REFERENCE_FIELDS:out[name[:-12]]=item
        elif name.endswith('_encoded_hex'):out[name[:-12]+'_raw_hex']=item
        else:out[name]=restore_value(item,base)
    return out


def restore_node(row,base):
    if 'address' in row:return row
    result=restore_value(row,base);result['address']=reference_va(row['id'],base)
    for field in ('handler_candidate','action_function','action_registry_entry','nvgen_callback_candidate',
                  'keyword_address','privilege_record_address','privilege_descriptor_address','option_privilege_address'):
        if isinstance(row.get(field),dict):result[field]=reference_va(row[field],base)
    accept=reference_va(row['links']['accept'],base);alternate=reference_va(row['links']['alternate'],base)
    result['raw_hex']=accept.to_bytes(8,'little').hex()+alternate.to_bytes(8,'little').hex()
    result['link_serialization']='Derived accept/alternate links only; original record bytes not reconstructed'
    return result


def adjacency(graph):
    return {n['address']:[edge['target'] for edge in semantic_options(n,(None,None,None),graph)] for n in graph['nodes']}


def reach(root,edges,nodes,max_nodes=500000):
    seen={root};pending=deque([root]);terminals=set();unread=set()
    while pending and len(seen)<=max_nodes:
        ea=pending.popleft();node=nodes.get(ea)
        if not node or node.get('status')=='unresolved':unread.add(ea)
        if node and node.get('path_semantics') in ('terminal','parameter_terminal') and not node.get('semantic_error'):
            terminals.add(ea)
        for target in edges.get(ea,()):
            if target not in seen:seen.add(target);pending.append(target)
    return {'seen':seen,'terminals':terminals,'unread':unread,'pending':list(pending),'limited':bool(pending)}


def registration_edges(registrations,slots,nodes,base,sentinel_rva):
    by_key=defaultdict(list)
    for slot in slots:
        if 'key' in slot and 'anchor' in slot:by_key[slot['key']].append(slot)
    edges=defaultdict(list);gaps=[]
    for reg in registrations:
        root=base+reg['root_rva'];key=base+reg['key_rva'];matches=by_key.get(key,[])
        if not matches:gaps.append({'registration_rva':reg['registration_rva'],'reason':'No acquired matching slot'})
        for slot in matches:
            source,target=slot['anchor'],root
            if slot.get('type')==2:
                source,target=root,slot['anchor']
                if raw_links(nodes.get(source,{}))[1]!=base+sentinel_rva:
                    gaps.append({'registration_rva':reg['registration_rva'],'reason':'Type-2 sentinel precondition not observed'})
                    continue
            elif slot.get('type')!=1:
                gaps.append({'registration_rva':reg['registration_rva'],'reason':'Unknown slot type'});continue
            edges[source].append({'source':source,'target':target,'kind':'candidate_registration_installation',
                'registration_rva':reg['registration_rva'],'key_rva':reg['key_rva'],'slot_type':slot['type'],
                'slot_source':slot.get('source','historical_slot'),'slot_creation_call_rva':slot.get('creation_call_rva'),
                'historical_registration_status':reg['runtime_status'],'conditions_evaluated':False})
    return dict(edges),gaps


def classify_cohort(graph,modes,ancestry,cohort,registrations,slots,base,sentinel_rva=0x3cb665c8,static_link_creations=()):
    nodes={n['address']:n for n in graph['nodes']};edges=adjacency(graph)
    root_modes=defaultdict(list)
    for mode in modes:
        if mode.get('root_rva') is not None:root_modes[base+mode['root_rva']].append(mode)
    mode_rows=[];observed=defaultdict(list);overlay_members=defaultdict(list);static_members=defaultdict(list);root_results={}
    overlays,binding_gaps=registration_edges(registrations,slots,nodes,base,sentinel_rva)
    static_slots=[{'key':base+s['key_rva'],'anchor':base+s['anchor_rva'],'type':s['type'],
        'source':'static_link_creation_candidate','creation_call_rva':s['call_rva']} for s in static_link_creations
        if s.get('key_rva') is not None and s.get('anchor_rva') is not None]
    static_edges,static_gaps=registration_edges(registrations,static_slots,nodes,base,sentinel_rva)
    augmented={ea:list(targets) for ea,targets in edges.items()}
    for source,items in overlays.items():augmented.setdefault(source,[]).extend(e['target'] for e in items)
    static_augmented={ea:list(targets) for ea,targets in augmented.items()}
    for source,items in static_edges.items():static_augmented.setdefault(source,[]).extend(e['target'] for e in items)
    for root,definitions in root_modes.items():
        result=reach(root,edges,nodes);candidate=reach(root,augmented,nodes);static_candidate=reach(root,static_augmented,nodes)
        root_results[root]={'observed':result,'overlay':candidate}
        for mode in definitions:
            observed_terminals=result['terminals']&cohort
            overlay_terminals=candidate['terminals']&cohort
            for ea in observed_terminals:observed[ea].append(mode['id'])
            for ea in overlay_terminals-observed_terminals:overlay_members[ea].append(mode['id'])
            for ea in (static_candidate['terminals']&cohort)-overlay_terminals:static_members[ea].append(mode['id'])
            mode_rows.append({'mode_id':mode['id'],'name':mode['name'],'prompt':mode['prompt'],'parent':mode['parent'],
                'root_rva':mode['root_rva'],'configuration_family_candidate':ancestry[mode['id']]['configuration_family_candidate'],
                'observed_projection_terminals':len(result['terminals']),'cohort_observed':len(observed_terminals),
                'cohort_with_registration_candidates':len(overlay_terminals),'unread_projection_targets':len(result['unread']),
                'cohort_with_static_link_creation_candidates':len(static_candidate['terminals']&cohort),
                'projection_limited':result['limited'] or candidate['limited'] or static_candidate['limited']})
        # Keep only the information needed below, rather than every mode's complete visited set.
        root_results[root]={'observed_terminals':result['terminals'],'overlay_terminals':candidate['terminals']}
    associations=defaultdict(list);reg_roots=defaultdict(list)
    for reg in registrations:reg_roots[base+reg['root_rva']].append(reg)
    for root,items in reg_roots.items():
        targets=reach(root,edges,nodes)['terminals']&cohort
        for ea in targets:
            for reg in items:
                associations[ea].append({'registration_rva':reg['registration_rva'],'key_rva':reg['key_rva'],
                    'runtime_status':reg['runtime_status'],'observed_binding':bool(reg.get('observed_binding_evidence'))})
    config_ids={m['id'] for m in modes if ancestry[m['id']]['configuration_family_candidate']}
    records=[];categories=Counter()
    for ea in sorted(cohort):
        obs=observed[ea];overlay=overlay_members[ea];static=static_members[ea];regs=associations[ea]
        if set(obs)&config_ids:category='additional_config_mode_root'
        elif obs:category='additional_other_mode_root'
        elif set(overlay)&config_ids:category='config_candidate_registration_edge'
        elif overlay:category='other_mode_candidate_registration_edge'
        elif set(static)&config_ids:category='config_static_slot_creation_candidate'
        elif static:category='other_mode_static_slot_creation_candidate'
        elif any(r['runtime_status']=='observed_pending' for r in regs):category='pending_fragment_without_mode_path'
        elif any(r['observed_binding'] for r in regs):category='bound_fragment_without_acquired_mode_path'
        elif regs:category='registration_fragment_without_acquired_mode_path'
        else:category='no_acquired_mode_or_registration_path'
        categories[category]+=1
        node=nodes[ea]
        records.append({'eol_va':ea,'handler_va':node.get('handler_candidate'),'selector_candidate':node.get('selector_candidate'),
            'category':category,'observed_mode_candidates':obs,'registration_overlay_mode_candidates':overlay,
            'static_slot_creation_mode_candidates':static,
            'registration_root_associations':regs,'remaining_uncertainties':node.get('remaining_uncertainties',[]),
            'availability':'Mode roots/graph connections are candidates; call conditions and registration activation unresolved'})
    return {'records':records,'mode_summary':mode_rows,'categories':dict(categories),
            'registration_candidate_edges':overlays,'registration_gaps':binding_gaps,
            'static_slot_creation_edges':static_edges,'static_slot_creation_gaps':static_gaps,
            'root_terminal_sets':root_results,'scope':'Original cohort retained; semantic graph and speculative registration edges reported separately'}
