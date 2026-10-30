"""Recover parser-mode candidates from reviewed factory call arguments."""
from collections import defaultdict


def address_constant(expr):
    if not isinstance(expr,dict):return None
    kind=expr.get('kind')
    if kind=='number':return expr['value']
    if kind=='global':return expr['ea']
    if kind in ('cast','ref'):return address_constant(expr.get('arg'))
    if kind=='binary':
        left=address_constant(expr.get('left'));right=address_constant(expr.get('right'))
        if left is None or right is None:return None
        operations={'add':lambda:left+right,'sub':lambda:left-right,'or':lambda:left|right,
                    'and':lambda:left&right,'xor':lambda:left^right}
        return operations.get(expr.get('op'),lambda:None)()
    return None


def compact_ir(value):
    if isinstance(value,list):return [compact_ir(v) for v in value]
    if isinstance(value,dict):return {k:compact_ir(v) for k,v in value.items() if k not in ('ea','code','capture_ea')}
    return value


def recover_mode_definitions(functions,identity,profile,read_string,image_ranges):
    if identity['input_md5']!=profile['input_md5']:raise ValueError('Mode consumer profile identity differs')
    base=identity['imagebase'];factories={int(x,0) if isinstance(x,str) else x for x in profile['factory_rvas']}
    records=[];errors=[]
    for function in functions:
        if function.get('error') or function.get('truncated'):
            errors.append({'function_rva':function['rva'],'error':function.get('error','ctree traversal truncated')})
        for event in function.get('events',[]):
            if event.get('kind')!='call' or event.get('target') not in factories:continue
            row={'call_rva':event.get('site_rva'),'caller_rva':function['rva'],'factory_rva':event['target'],
                 'guards':compact_ir(event.get('guards',[])),'conditions_complete':False,'gaps':[]}
            args=event.get('args',[])
            for field,index in profile['arguments'].items():
                expr=args[index] if index<len(args) else None
                value=address_constant(expr)
                if value==0:
                    row[field+'_rva' if field=='root' else field]=None
                    continue
                va=(value&0x7fffffffffffffff) if value is not None else None
                rva=va-base if va is not None else None
                if rva is None or not any(lo<=rva<hi for lo,hi in image_ranges):
                    row[field+'_rva' if field=='root' else field]=None
                    row['gaps'].append({'field':field,'reason':'Pointer expression unresolved or outside this image',
                                        'expression':compact_ir(expr)})
                elif field=='root':row['root_rva']=rva
                else:
                    try:
                        row[field]=read_string(rva)
                        row[field+'_string_rva']=rva
                    except (ValueError,KeyError) as exc:
                        row[field]=None;row['gaps'].append({'field':field,'rva':rva,'reason':str(exc)})
            records.append(row)
    # Preserve distinct definitions for reused names, roots and conditional call sites.
    groups=defaultdict(list)
    for row in records:
        signature=tuple(row.get(k) for k in ('name','prompt','parent','root_rva'))
        if row.get('name') is None:signature+=('unresolved-call',row['call_rva'])
        groups[signature].append(row)
    modes=[]
    for index,items in enumerate(groups.values()):
        first=items[0]
        modes.append({'id':'mode-%04d'%index,**{k:first.get(k) for k in ('name','prompt','parent','description','root_rva')},
            'definition_evidence':items,'availability':'Static factory-call candidate; registration/conditions not executed'})
    return {'modes':modes,'calls':len(records),'functions_with_errors':errors,'conditions_evaluated':False}


def configuration_ancestry(modes):
    parents=defaultdict(set)
    for mode in modes:
        if mode.get('name') and mode.get('parent'):parents[mode['name']].add(mode['parent'])
    result={}
    for mode in modes:
        pending=[mode.get('name'),mode.get('parent')];seen=set();found=False
        while pending:
            name=pending.pop()
            if not name or name in seen:continue
            seen.add(name)
            if name=='configure':found=True;break
            pending.extend(parents.get(name,()))
        result[mode['id']]={'configuration_family_candidate':found,'ancestry_names':sorted(seen),
            'method':'Explicit factory parent names; alternatives retained; current mode activation unresolved'}
    return result


def recover_link_creations(functions,identity,profile,image_ranges):
    """Retain conditional static create-link calls, independently of observed slot records."""
    if identity['input_md5']!=profile['input_md5']:raise ValueError('Link consumer profile identity differs')
    base=identity['imagebase'];apis={int(a['rva'],0):a for a in profile.get('link_creation_apis',[])};records=[]
    for function in functions:
        for event in function.get('events',[]):
            if event.get('kind')!='call' or event.get('target') not in apis:continue
            api=apis[event['target']];args=event.get('args',[])
            row={'call_rva':event.get('site_rva'),'caller_rva':function['rva'],'api_rva':event['target'],
                 'type':api['type'],'guards':compact_ir(event.get('guards',[])),'conditions_complete':False,'gaps':[]}
            for field,index in (('key',api['key_arg']),('anchor',api['root_arg'])):
                expr=args[index] if index<len(args) else None;value=address_constant(expr)
                rva=(value&0x7fffffffffffffff)-base if value is not None else None
                if rva is not None and any(lo<=rva<hi for lo,hi in image_ranges):row[field+'_rva']=rva
                else:
                    row[field+'_rva']=None;row['gaps'].append({'field':field,'expression':compact_ir(expr),'reason':'Unresolved image pointer'})
            records.append(row)
    return records
