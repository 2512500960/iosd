"""Reviewed IOS option-table layouts; never execute an iterator or producer.

The array adapter walks 24-byte entries. List adapters call a producer and may
return a reused scratch entry, so an observed scratch buffer is never treated
as the complete list. Reviewed producer models are data supplied by a profile.
"""
import re
from .memory import MemoryReadError,decode_pointer,read_cstring


def decode_options(memory,row,name,pointer_mode,image_base,models,max_entries=256):
    supported={'keyword_option_action','keyword_option_list_action','keyword_option_list_dynamic_action',
               'keyword_option_list_dynamic_mm_action','keyword_option_func_action','keyword_dynamic_option_func_action'}
    if name not in supported:return
    payload=row['payload'];size=36 if name=='keyword_dynamic_option_func_action' else 28
    raw=memory.read(payload,size);ptr=lambda off:decode_pointer(raw[off:off+8],pointer_mode)
    dynamic=name=='keyword_dynamic_option_func_action'
    is_array=name in ('keyword_option_action','keyword_option_func_action')
    has_getter=name!='keyword_option_action'
    destination=int.from_bytes(raw[16:18] if dynamic else raw[8:12] if is_array else raw[8:10],'big')
    width=(int.from_bytes(raw[18:20],'big') if dynamic else 4 if is_array else int.from_bytes(raw[10:12],'big'))
    privilege=ptr(24 if dynamic else 16);flags=int.from_bytes(raw[32:36] if dynamic else raw[24:28],'big')
    getter=ptr(0) if has_getter else None
    row.update(path_semantics='keyword_options',semantic_role='keyword_options',descriptor_raw_hex=raw.hex(),
        keyword_options=[],option_frontiers=[],option_enumeration_complete=False,option_privilege_address=privilege,
        option_storage={'field_offset':destination,'declared_width':width,'width_candidate':8 if width==8 else 4,'operation':'or' if flags&0x4000000 else 'string_copy' if flags&0x10000 else 'assign',
                        'flags_raw_hex':flags.to_bytes(4,'big').hex()},
        option_source={'kind':'array' if not has_getter else 'producer_callback','getter':getter,'producer_executed':False,
                       'release_callback':ptr(8) if dynamic else None,'dynamic_scratch_entry':dynamic or 'dynamic' in name},
        semantic_status='Consumer-validated option-table alternatives; producer/context/privilege constraints retained')
    if name=='keyword_option_func_action':
        row['option_wrapper_condition']={'kind':'parser_field_mask_zero','field_offset':0x28C2,'width':1,'mask':1,'evaluated':False}
    if dynamic:
        row['option_string_storage_offset']=width
        row['option_storage']['width_candidate']=4
    def text(address,limit):return read_cstring(memory,address,limit) if address else ''
    def keep(keyword,value,help_text='',entry=None,raw_entry=None,minimum_match=0,conditions=()):
        item={'keyword':keyword,'value':value,'entry_address':entry,'minimum_match':minimum_match,
              'help':help_text,'conditions':list(conditions),'effects':[]}
        if raw_entry is not None:item['raw_hex']=raw_entry.hex()
        if not re.fullmatch(r'[^\x00-\x20\x7f]{1,96}',keyword):
            item['keyword_unparsed']=True;row['option_frontiers'].append({'address':entry,'reason':'Option keyword is not a single printable token','text':keyword})
        storage=row['option_storage'];offset=storage['field_offset']
        if offset not in (0xffff,0xffffffff):
            if storage['operation']=='string_copy':item['effects'].append({'kind':'constant_string_assignment','field_offset':offset,'value':keyword,'value_resolved':True,'consumes_input':False})
            else:item['effects'].append({'kind':'keyword_state_assignment','field_offset':offset,'width_candidate':storage['width_candidate'],
                'operation':storage['operation'],'value_raw_hex':int(value).to_bytes(8,'big').hex()})
        if flags&0x8000000 and not flags&0x10000:
            item['state_precondition']={'kind':'parser_state_mask_zero','field_offset':offset,'width_candidate':storage['width_candidate'],
                'mask_raw_hex':int(value if flags&0x4000000 else (1<<(8*min(storage['width_candidate'],8)))-1).to_bytes(8,'big').hex(),'evaluated':False}
        row['keyword_options'].append(item)
        return item
    def optional_help(address):
        try:return text(address,512),None
        except MemoryReadError as exc:return '',str(exc)
    def array(table):
        row['option_source']['table_address']=table
        if not table:
            row['option_enumeration_complete']=True;row['option_source']['current_table_empty']=True;return
        for index in range(max_entries):
            ea=table+24*index
            try:
                head=memory.read(ea,8);word=decode_pointer(head,pointer_mode)
                if not word:row['option_enumeration_complete']=True;return
                entry=memory.read(ea,24)
                help_text,error=optional_help(decode_pointer(entry[8:16],pointer_mode))
                item=keep(text(word,97),int.from_bytes(entry[16:20],'big'),help_text,ea,entry,int.from_bytes(entry[20:24],'big'))
                if error:item['help_error']=error
            except MemoryReadError as exc:row['option_frontiers'].append({'address':ea,'reason':str(exc)});return
        row['option_frontiers'].append({'address':table+24*max_entries,'reason':'option_entry_limit'})
    if not has_getter:array(ptr(0));return
    model=next((v for k,v in models.items() if int(k,0)==getter-image_base),None)
    if model is None:
        row['option_frontiers'].append({'address':getter,'reason':'Producer semantics unresolved; no function executed'});return
    row['option_source']['reviewed_model']=model
    kind=model['kind']
    if kind=='constant_array':array(image_base+int(model['table_rva'],0));return
    if kind=='indexed_strings':
        start=model.get('start',0);count=model['count']
        if not 0<count<=max_entries:raise ValueError('Reviewed option count exceeds bound')
        end=start+count
        if 'dynamic' in name and model.get('increment_previous_index'):
            start=max(start,1)
            row['option_source']['initial_previous_value']=0
            row['option_source']['initialization_note']='Dynamic wrapper passes a zeroed scratch record; producer increments previous index'
        for index in range(start,end):
            try:
                wp=decode_pointer(memory.read(image_base+int(model['names_rva'],0)+index*8,8),pointer_mode)
                hp=decode_pointer(memory.read(image_base+int(model['helps_rva'],0)+index*8,8),pointer_mode) if model.get('helps_rva') else 0
                help_text,error=optional_help(hp)
                item=keep(text(wp,97),index,help_text,conditions=[{'kind':'reviewed_option_producer','getter':getter,'index':index,'model_evidence':model.get('evidence'),'evaluated':False}])
                if error:item['help_error']=error
            except MemoryReadError as exc:row['option_frontiers'].append({'index':index,'reason':str(exc)})
        row['option_enumeration_complete']=not row['option_frontiers'];return
    if kind=='gated_choices':
        for choice in model['entries']:
            condition={'kind':'global_option_membership','variable_rva':choice['enabled_rva'],'evaluated':False}
            try:
                data=memory.read(image_base+int(choice['enabled_rva'],0),4);value=int.from_bytes(data,'big')
                condition.update(raw_hex=data.hex(),value=value,evaluated=True,snapshot_result=value!=0)
            except MemoryReadError as exc:condition['error']=str(exc)
            help_text=''
            if choice.get('help_pointer_rva'):
                try:
                    hp=decode_pointer(memory.read(image_base+int(choice['help_pointer_rva'],0),8),pointer_mode);help_text=text(hp,512)
                except MemoryReadError as exc:condition['help_error']=str(exc)
            keep(choice['keyword'],choice['value'],help_text,conditions=[condition])
        row['option_enumeration_complete']=True;return
    row['option_frontiers'].append({'address':getter,'reason':'Unsupported producer model kind: '+kind})
