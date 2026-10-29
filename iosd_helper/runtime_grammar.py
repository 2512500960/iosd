"""Reconstruct conditional grammar graphs from exact saved debugger pages.

Runtime pointers are tagged big-endian. Only the two transition links are also
serialized as little-endian VA for the existing symbolic path interpreter.
The original runtime record is retained separately. No static registration
overlay is installed into the observed graph.
"""
from collections import deque
from bisect import bisect_right
from .memory import MemoryReadError, decode_pointer,read_cstring
from .grammar_semantics import decode_action_payload, node_title


class CapturedPages:
    source='saved-debugger-pages'

    def __init__(self, captures):
        self.blocks={};self.missing_pages=set();self.conflicts=[]
        for capture in captures:
            for row in capture.get('ranges',[])+capture.get('cache_blocks',[]):
                if 'raw_hex' not in row:continue
                va=row['runtime_va'];raw=bytes.fromhex(row['raw_hex'])
                if len(raw)!=65536:continue
                old=self.blocks.get(va)
                if old is not None and old!=raw:self.conflicts.append(va)
                self.blocks[va]=raw
        self.starts=sorted(self.blocks)

    def read(self,address,size):
        if address<0 or size<0:raise ValueError('Negative memory range')
        chunks=[];end=address+size
        while address<end:
            index=bisect_right(self.starts,address)-1
            start=self.starts[index] if index>=0 else None
            raw=self.blocks.get(start) if start is not None else None
            if raw is None or address>=start+len(raw):
                missing=address&~65535;self.missing_pages.add(missing)
                raise MemoryReadError('Runtime page not captured at %#x'%missing)
            n=min(end-address,len(raw)-(address-start));chunks.append(raw[address-start:address-start+n]);address+=n
        return b''.join(chunks)


def reconstruct_runtime_graph(memory,static_graph,base,linkage,max_nodes=250000,keyword_gates=(),option_getters=None,predicate_models=None):
    actions={a['opcode']:{**a,'address':base+a['address'],'function':base+a['function'] if a['function'] else 0}
             for a in static_graph['action_registry']}
    dispatch=[]
    for opcode,action in actions.items():
        observed={'opcode':opcode,'name':action['name'],'entry_va':action['address'],
            'static_function_va':action['function'],'verified':False}
        try:
            raw=memory.read(action['address'],24)
            name=read_cstring(memory,decode_pointer(raw[8:16],'swap_then_mask'),128)
            number=int.from_bytes(raw[16:20],'big')
            observed.update(raw_hex=raw.hex(),runtime_name=name,runtime_opcode=number,
                runtime_function_va=decode_pointer(raw[:8],'swap_then_mask'))
            if name!=action['name'] or number!=opcode:observed['error']='Runtime action name/opcode mismatch'
            else:
                observed['verified']=True;action['function']=observed['runtime_function_va']
        except MemoryReadError as exc:observed['error']=str(exc)
        action['dispatch_observation']=observed;dispatch.append(observed)
    queue=deque(base+n['address'] for n in static_graph['nodes']);queued=set(queue)
    for chain in linkage['lists']:
        for record in chain['nodes']:
            field='anchor' if chain['name']=='dynamic_parser_linkage' else 'fragment'
            target=record['fields'][field]['value']
            if target and target not in queued:queue.append(target);queued.add(target)
    nodes=[];edges=[]
    while queue and len(nodes)<max_nodes:
        ea=queue.popleft();row={'address':ea,'status':'unresolved','handler_candidate':None,'source':'saved-debugger-pages'}
        if 0<=ea-base<0x50000000:row['image_rva']=ea-base
        nodes.append(row)
        try:raw=memory.read(ea,40)
        except MemoryReadError as exc:row['reason']=str(exc);continue
        row['runtime_raw_hex']=raw.hex()
        if not any(raw):row['reason']='Zero runtime record; terminal semantics unresolved';continue
        opcode=int.from_bytes(raw[16:20],'big');row['opcode']=opcode
        if opcode not in actions:
            row['reason']='Opcode absent from reviewed action registry';continue
        accept=decode_pointer(raw[:8],'swap_then_mask');alternate=decode_pointer(raw[8:16],'swap_then_mask')
        row.update(status='transition_candidate',raw_hex=(accept.to_bytes(8,'little')+alternate.to_bytes(8,'little')+raw[16:]).hex(),
                   payload=decode_pointer(raw[24:32],'swap_then_mask'),condition_semantics='unresolved')
        decode_action_payload(memory,row,actions[opcode],'swap_then_mask',image_base=base,option_models=option_getters)
        row['action_dispatch_observation']=actions[opcode]['dispatch_observation']
        if not row['action_dispatch_observation']['verified']:
            row['dispatch_semantics_unverified']=True
        if row.get('semantic_role')=='no_argument_predicate':
            callback=row['condition']['callback']
            model=next((m for k,m in (predicate_models or {}).items() if int(k,0)==callback-base),None)
            if model:
                row['condition']['reviewed_model']=model
                if model['kind']=='global_comparison':
                    row['effects']=[e for e in row.get('effects',[]) if e.get('kind')!='context_callback']
                    row.pop('branch_gap',None)
                    try:
                        data=memory.read(base+int(model['variable_rva'],0),model.get('size',4));value=int.from_bytes(data,model.get('encoding','big'))
                        result=value==model['equals']
                        row['condition'].update(snapshot_result=result,observed_value=value,observed_raw_hex=data.hex(),
                            evaluation_source='Saved memory plus reviewed pure return expression; callback not executed',evaluated=True)
                    except MemoryReadError as exc:row['condition']['read_error']=str(exc)
                elif model['kind']=='registry_or_callback':
                    try:
                        data=memory.read(base+int(model['fallback_pointer_rva'],0),8)
                        row['condition'].update(observed_fallback_target=decode_pointer(data,'swap_then_mask'),fallback_pointer_raw_hex=data.hex())
                    except MemoryReadError as exc:row['condition']['read_error']=str(exc)
        if row.get('path_semantics') in ('keyword','keyword_options') and keyword_gates:
            descriptor=bytes.fromhex(row.get('descriptor_raw_hex',''))
            if len(descriptor)>=24:
                privilege=row.get('option_privilege_address') if row.get('path_semantics')=='keyword_options' else decode_pointer(descriptor[16:24],'swap_then_mask')
                row['privilege_record_address']=privilege
                try:
                    flags=memory.read(privilege,12);row['privilege_record_raw_hex']=flags.hex()
                    native=int.from_bytes(flags[:8],'little')
                    for gate in keyword_gates:
                        mask=int(gate['descriptor_native_u64_mask'],0)
                        if not native&mask:continue
                        evidence={**gate,'variable_runtime_va':base+int(gate['variable_rva'],0),'evaluated':False}
                        try:
                            raw_state=memory.read(evidence['variable_runtime_va'],gate.get('variable_size',4))
                            value=int.from_bytes(raw_state,gate.get('variable_encoding','big'))
                            evidence.update(evaluated=True,value=value,raw_hex=raw_state.hex(),direct_gate_passes=value!=0)
                        except MemoryReadError as exc:evidence['error']=str(exc)
                        row.setdefault('keyword_access_gates',[]).append(evidence)
                except MemoryReadError as exc:row['privilege_record_error']=str(exc)
        row['display_label']=node_title(row)
        targets=[(accept,'runtime_accept_pointer'),(alternate,'runtime_alternate_pointer')]
        targets.extend((e['target'],e['kind']) for e in row.get('semantic_edges',[]))
        for target,kind in targets:
            if not target:continue
            edges.append({'source':ea,'target':target,'kind':kind,'evidence':'saved runtime bytes; execution condition unresolved'})
            if target not in queued:queue.append(target);queued.add(target)
    settings=dict(static_graph.get('path_analysis',{}))
    callbacks=settings.get('reviewed_normal_cli_callbacks',[])
    settings['reviewed_normal_cli_callback_rvas']=list(callbacks)
    settings['reviewed_normal_cli_callbacks']=[hex(base+(int(v,0) if isinstance(v,str) else v)) for v in callbacks]
    return {'source':memory.source,'nodes':nodes,'edges':edges,'registrations':[],'link_registry':[],
            'dynamic_link_definitions':[],'link_registry_errors':[],'action_registry':list(actions.values()),
            'mode_definitions':[{**m,'root':hex(base+int(m['root'],0)),'evidence_call':hex(base+int(m['evidence_call'],0))} for m in static_graph['mode_definitions']],
            'mode_evidence':static_graph.get('mode_evidence',{}),'path_analysis':settings,
            'stop_reason':'node_limit' if queue else 'exhausted_acquired_structural_targets',
            'pending_addresses':list(queue),'warning':'Observed connections plus symbolic conditions; not a list of commands guaranteed executable',
            'runtime_action_dispatch':dispatch,
            'pointer_serialization':'runtime_raw_hex is original; raw_hex has only accept/alternate converted to little-endian VA for symbolic interpretation'}


def observe_slot_bindings(memory,static_graph,base,linkage,sentinel_rva,max_chain=50000):
    """Observe DEF70B0 type-1 alternate chains and type-2 rewritten links.

    Same-key/root evidence is kept distinct from mode-wide root reachability.
    A negative result never proves absence when a chain/page is incomplete.
    """
    slots=[];by_key={};installed={};sentinel=base+sentinel_rva
    static_nodes={n['address']:n for n in static_graph['nodes']}
    for source in static_graph.get('link_registry',[]):
        va=base+source['address'];slot={'source':'core_registry','record_va':va,'frontiers':[]}
        try:
            raw=memory.read(va,48)
            slot.update(raw_hex=raw.hex(),key=decode_pointer(raw[:8],'swap_then_mask'),
                        anchor=decode_pointer(raw[16:24],'swap_then_mask'),type=int.from_bytes(raw[24:28],'big'))
        except MemoryReadError as exc:slot['frontiers'].append({'reason':str(exc)})
        slots.append(slot)
    for chain in linkage['lists']:
        if chain['name']!='dynamic_parser_linkage':continue
        for record in chain['nodes']:
            slots.append({'source':'dynamic_registry','record_va':record['address'],
                'key':record['fields']['key']['value'],'anchor':record['fields']['anchor']['value'],
                'type':record['fields']['type']['value'],'frontiers':[]})
    for slot in slots:
        if 'key' not in slot:continue
        by_key.setdefault(slot['key'],[]).append(slot)
        if slot['type']!=1:continue
        current=slot['anchor'];seen=set();chain=[]
        while current and current!=sentinel:
            if current in seen:slot['frontiers'].append({'address':current,'reason':'alternate_chain_cycle'});break
            if len(seen)>=max_chain:slot['frontiers'].append({'address':current,'reason':'alternate_chain_limit'});break
            seen.add(current);chain.append(current)
            try:raw=memory.read(current,16)
            except MemoryReadError as exc:slot['frontiers'].append({'address':current,'reason':str(exc)});break
            current=decode_pointer(raw[8:16],'swap_then_mask')
        slot['alternate_chain']=chain
        slot['reached_sentinel']=current==sentinel
        for root in seen:installed.setdefault((slot['key'],root),[]).append(slot['record_va'])
    comparisons=[]
    for reg in static_graph['registrations']:
        key=base+reg['link_key'];root=base+reg['root'];matches=[];unknown=[]
        for va in installed.get((key,root),[]):matches.append({'slot_record_va':va,'kind':'observed_type1_alternate_chain_membership'})
        for slot in by_key.get(key,[]):
            if slot['type']!=2:continue
            try:
                raw=memory.read(root+8,8);actual=decode_pointer(raw,'swap_then_mask')
                old=static_nodes.get(reg['root'])
                old_raw=bytes.fromhex(old.get('raw_hex','')) if old else b''
                original=int.from_bytes(old_raw[8:16],'little') if len(old_raw)>=16 else None
                if actual==slot['anchor']:
                    matches.append({'slot_record_va':slot['record_va'],'kind':'observed_type2_alternate_pointer','original_was_sentinel':original==sentinel_rva})
            except MemoryReadError as exc:unknown.append({'reason':str(exc)})
        comparisons.append({'registration_rva':reg['address'],'key_rva':reg['link_key'],'root_rva':reg['root'],
            'runtime_key':key,'runtime_root':root,'observed_binding_evidence':matches,'unknown':unknown,
            'matching_slots_observed':len(by_key.get(key,[])),'absence_proven':False})
    return slots,comparisons
