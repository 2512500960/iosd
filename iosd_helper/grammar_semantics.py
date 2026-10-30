"""Sample-validated action metadata and payload decoders. Never execute predicates."""
import re
from .memory import MemoryReadError, decode_pointer, read_cstring


def keyword_literal(row,text):
    """Retain printable descriptor strings, including punctuation and embedded spaces."""
    if not 1<=len(text)<=80 or not text.strip() or not all(32<=ord(c)<127 for c in text):
        row['keyword_text_unparsed']=text
        raise MemoryReadError('Keyword descriptor exceeds printable literal bounds')
    row['keyword_match_unit']='descriptor_literal'
    if not re.fullmatch(r'[A-Za-z0-9_.:/+<>-]{1,80}',text):
        row['keyword_literal_shape']='punctuation_or_embedded_space'
        row.setdefault('keyword_extra_conditions',[]).append({'kind':'descriptor_literal_matching',
            'literal':text,'wrapper_whitespace_and_match_flags_symbolic':True,'evaluated':False})
        row['keyword_gap']='Descriptor literal retained; whitespace and matching flags remain symbolic'
    return text


def read_action_registry(memory, base, count):
    if not 1 <= count <= 1024:
        raise ValueError("Invalid action registry count")
    rows, errors = [], []
    for index in range(count):
        ea = base + index * 24
        try:
            raw = memory.read(ea, 24)
            function = decode_pointer(raw[:8], "little")
            name_ptr = decode_pointer(raw[8:16], "little")
            opcode = int.from_bytes(raw[16:20], "big")
            if opcode != index:
                raise MemoryReadError("Action registry opcode/index mismatch")
            name = read_cstring(memory, name_ptr, 128)
            if not re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", name):
                raise MemoryReadError("Invalid action name")
            rows.append({"address": ea, "opcode": opcode, "name": name,
                         "function": function, "raw_hex": raw.hex(),
                         "runtime_function_required": function == 0})
        except MemoryReadError as exc:
            errors.append({"address": ea, "error": str(exc)})
    return rows, errors


def decode_action_payload(memory, row, action, pointer_mode="little", function_resolver=None,
                          image_base=0,option_models=None):
    """Attach semantics only to action names whose consumers were inspected."""
    name, payload = action["name"], row["payload"]
    row.update(action_name=name, action_function=action["function"],
               action_registry_entry=action["address"],
               action_function_requires_runtime=action["function"] == 0,
               semantic_status="action registry mapped; payload semantics unresolved")
    if name in ("keyword_sk_off_action", "keyword_sk_on_action", "keyword_optws_action"):
        row["reviewed_keyword_wrapper"]={"name":name,
            "behavior":"Copies the first 24 descriptor bytes into keyword_core; assignment offset is 0xffff; wrapper flags remain uninterpreted",
            "evidence":"Reviewed 26.01.02 wrapper named in action registry; normal CLI branch copies keyword descriptor"}
        name="keyword_action"
    elif name in ("keyword_orset_action", "keyword_ortest_action", "keyword_orset_mm_action", "keyword_ortest_mm_action"):
        row["reviewed_keyword_wrapper"]={"name":name,
            "behavior":"Copies keyword/id descriptor; OR assignment, with an additional zero-mask precondition for ortest",
            "evidence":"Reviewed 26.01.02 ORSET/ORTEST wrappers and E38DB80 consumer; exact wrapper address retained in action registry"}
        name="keyword_id_mm_action" if '_mm_' in name else "keyword_id_action"
    control = {"NONE_action": "stop", "NOP_action": "epsilon_both",
               "link_point_action": "epsilon_both", "link_trans_action": "epsilon_links",
               "help_action": "epsilon_alternate", "link_point_error_action": "stop",
               "noprefix_action": "sense_choice", "comment_action": "epsilon_accept"}
    if name in control:
        row["path_semantics"] = control[name]
    if name in ("NONE_action", "NOP_action", "link_point_action", "link_point_error_action", "link_trans_action"):
        row["semantic_role"] = "link_or_control"
    if name == "deprecated_action":
        row.update(path_semantics="epsilon_accept", semantic_role="parser_state_marker",
                   effects=[{"kind": "parser_state_assignment", "field_offset": 0x301c,
                             "width_candidate": 4, "operation": "assign", "value_raw_hex": "00000001",
                             "consumes_input": False}],
                   semantic_status="Reviewed normal CLI consumer E38D8A0: mark state and accept; downstream use of marker unresolved")
        return
    if name == "whitespace_action":
        row.update(path_semantics="whitespace", semantic_role="input_separator",
                   whitespace={"nvgen_field": 9636, "input_offset_field": 12124,
                               "character_table_rva": 0x7a139e0, "class_mask": 8,
                               "boundary_codes": [0, 33, 59], "boundary_requires_field_zero": 11960,
                               "consumption": "DEF4DC0 temporarily advances input offset while scheduling accept"},
                   semantic_status="Reviewed E393260/DEF4DC0 normal CLI: alternate first; NVGEN bypass or input-dependent accept")
        return
    if not payload:
        return
    def ptr(raw, off=0):
        return decode_pointer(raw[off:off + 8], pointer_mode)
    def function(value):
        return function_resolver(value) if function_resolver and value else None
    try:
        if name == "link_trans_action" and payload < (1 << 47):
            row["semantic_edges"] = [{"target": payload, "kind": "link_extra_candidate",
                                      "field_address": row["address"] + 24}]
        if name == 'general_keyword_action':
            raw=memory.read(payload,48);keyword=read_cstring(memory,ptr(raw),96)
            keyword_literal(row,keyword)
            row.update(path_semantics='keyword',semantic_role='keyword',keyword_candidate=keyword,
                keyword_address=ptr(raw),descriptor_raw_hex=raw.hex(),
                privilege_descriptor_address=ptr(raw,16),minimum_match_candidate=int.from_bytes(raw[40:44],'big'),
                keyword_flags_raw_hex=raw[44:48].hex(),
                keyword_extra_conditions=row.get('keyword_extra_conditions',[])+[{'kind':'general_keyword_flags_and_privilege','evaluated':False,
                    'flags_raw_hex':raw[44:48].hex(),'privilege_descriptor_address':ptr(raw,16),
                    'minimum_match_candidate':int.from_bytes(raw[40:44],'big')}],
                keyword_gap='General keyword flags, access gates and state operation remain symbolic',
                semantic_status='Reviewed E38DB80 keyword fields and control branches; flags and effects retained')
            offset=int.from_bytes(raw[24:26],'big')
            if offset!=0xffff:
                row['effects']=[{'kind':'general_keyword_storage','storage_offset_candidate':offset,
                    'width_candidate':int.from_bytes(raw[26:28],'big'),'value_raw_hex':raw[32:40].hex(),
                    'operation':'controlled_by_flags','effects_unresolved':True}]
            if ptr(raw,8):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,8),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name in ("keyword_action", "keyword_id_action", "keyword_mm_action", "keyword_id_mm_action"):
            size = {"keyword_action": 24, "keyword_id_action": 40,
                    "keyword_mm_action": 28, "keyword_id_mm_action": 44}[name]
            raw = memory.read(payload, size)
            row["descriptor_raw_hex"] = raw.hex()
            keyword = read_cstring(memory, ptr(raw), 96)
            keyword_literal(row,keyword)
            row.update(keyword_candidate=keyword, keyword_address=ptr(raw),
                       path_semantics="keyword",
                       descriptor_raw_hex=raw.hex(), semantic_role="keyword",
                       semantic_status="consumer-validated keyword descriptor",
                       privilege_descriptor_raw_hex=raw[16:24].hex())
            if "_mm_" in name:
                offset = 40 if name == "keyword_id_mm_action" else 24
                row["minimum_match_candidate"] = int.from_bytes(raw[offset:offset + 4], "big")
            if name.startswith("keyword_id"):
                row["effects"] = [{"kind": "keyword_state_assignment", "field_offset": int.from_bytes(raw[24:26], "big"),
                                   "width_candidate": int.from_bytes(raw[26:28], "big"),
                                   "value_raw_hex": raw[32:40].hex(), "evaluated": False}]
                if action['name'] in ('keyword_orset_action','keyword_ortest_action','keyword_orset_mm_action','keyword_ortest_mm_action'):
                    row['effects'][0]['operation']='or'
                if action['name'] in ('keyword_ortest_action','keyword_ortest_mm_action'):
                    row['keyword_state_precondition']={'kind':'parser_state_mask_zero',
                        'field_offset':int.from_bytes(raw[24:26],'big'),'width_candidate':int.from_bytes(raw[26:28],'big'),
                        'mask_raw_hex':raw[32:40].hex(),'evaluated':False}
            if ptr(raw, 8):
                try:
                    row["help_candidate"] = read_cstring(memory, ptr(raw, 8), 512)
                except MemoryReadError as exc:
                    row["help_error"] = str(exc)
        elif name in ("eolns_action", "eolns_command_action", "eols_action", "eols_command_action"):
            raw = memory.read(payload, 16)
            handler = ptr(raw)
            flags_offset = 8 if name == "eolns_command_action" else 12
            row.update(semantic_role="command_terminal", handler_candidate=handler,
                       path_semantics="terminal",
                       handler_field=payload, handler_metadata=function(handler),
                       descriptor_raw_hex=raw.hex(),
                       selector_candidate=int.from_bytes(raw[8:12], "big") if name.startswith("eols_") else 0,
                       command_flags_raw_hex=raw[flags_offset:flags_offset + 4].hex(),
                       command_flags_field=payload + flags_offset,
                       semantic_status="consumer-validated EOL handler field; runtime gates remain unresolved")
        elif name == "nvgens_action":
            raw = memory.read(payload, 16)
            callback = ptr(raw)
            row.update(semantic_role="configuration_generation", nvgen_callback_candidate=callback,
                       path_semantics="epsilon_accept",
                       nvgen_callback_metadata=function(callback), descriptor_raw_hex=raw.hex(),
                       semantic_status="consumer-validated NVGEN callback; not a command terminal")
        elif name == 'timesec_action':
            raw=memory.read(payload,24);second=int.from_bytes(raw[8:12],'big');total=int.from_bytes(raw[12:16],'big')
            row.update(path_semantics='parameter',semantic_role='time_parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'time_hm' if second==0xffffffff else 'time_hms',
                    'hour_storage_offset':int.from_bytes(raw[:4],'big'),'minute_storage_offset':int.from_bytes(raw[4:8],'big'),
                    'second_storage_offset':None if second==0xffffffff else second,
                    'total_seconds_storage_offset':None if total==0xffffffff else total,
                    'hours':[0,23],'minutes':[0,59],'seconds':[0,59],'separator':':'},
                parameter_condition={'kind':'time_input_and_context','evaluated':False},
                parameter_gap='Input boundary/help context and time matching are symbolic',
                semantic_status='Reviewed E3A8BA0 hour/minute/optional-second fields and optional seconds-total assignment')
            if ptr(raw,16):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,16),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name == 'signed_number_action':
            raw=memory.read(payload,24);bounds=[int.from_bytes(raw[i:i+4],'big',signed=True) for i in (4,8)]
            row.update(path_semantics='parameter',semantic_role='signed_number_parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'signed_number','storage_offset':int.from_bytes(raw[:4],'big'),
                    'min':min(bounds),'max':max(bounds),'declared_bounds':bounds,'storage_width':4},
                parameter_condition={'kind':'signed_decimal_input_and_boundary','evaluated':False},
                semantic_status='Reviewed E3975B0 signed decimal bounds, overflow checks and four-byte storage')
            if ptr(raw,16):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,16),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name in ('hexdata_action','hexdata_action_even'):
            raw=memory.read(payload,24);mode=int.from_bytes(raw[20:24],'big')
            row.update(path_semantics='parameter',semantic_role='hex_parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'hexstring' if mode==0 else 'hexdata',
                    'storage_offset':int.from_bytes(raw[:2],'big'),'length_storage_offset':int.from_bytes(raw[2:4],'big'),
                    'declared_limit':int.from_bytes(raw[16:20],'big'),'mode_raw_hex':raw[20:24].hex(),
                    'initial_character_run_even_required':name=='hexdata_action_even'},
                parameter_condition={'kind':'hex_parse_and_boundary','parser_rva':0xe3a4ef0,
                    'even_initial_run':name=='hexdata_action_even','character_class_mask':0x44,'evaluated':False},
                parameter_gap='Hex parser mode, size unit and input/context validation retained for further review',
                semantic_status='Reviewed E3A5130 descriptor and E3A5610 parity wrapper; helper validation retained')
            if ptr(raw,8):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,8),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name == 'gen_number_func_action':
            raw=memory.read(payload,28);callback=ptr(raw,8)
            row.update(path_semantics='parameter',semantic_role='number_parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'unsigned_number_dynamic' if callback else 'unsigned_number',
                    'storage_offset':int.from_bytes(raw[:4],'big'),'min':0,'max':0xffffffff,
                    'bounds_callback':callback,'bounds_evaluated':not bool(callback),'default_bounds_only':bool(callback),
                    'flags_raw_hex':raw[24:28].hex()},
                parameter_condition={'kind':'general_number_callback_and_context','callback':callback,
                    'callback_gate_fields':[0x2ebc,0x2ec0,0x3510],'evaluated':False},
                parameter_gap='Callback-provided numeric bounds and general-number flags remain symbolic',
                semantic_status='Reviewed E398350 default bounds and conditional callback before E395CC0')
            if ptr(raw,16):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,16),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name in ('url_action','url_exact_action'):
            raw=memory.read(payload,40 if name=='url_action' else 32)
            row.update(path_semantics='parameter',semantic_role='url_parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'url_dynamic','storage_offset':int.from_bytes(raw[:2],'big',signed=True),
                    'descriptor_fields_raw_hex':raw[:24].hex(),'exact_wrapper':name=='url_exact_action'},
                parameter_condition={'kind':'url_registry_mode_and_input','mode_gate_rva':0xd651810,
                    'parser_rva':0xd65d690,'registry_getter_rva':0xd72c550,'evaluated':False},
                parameter_gap='URL scheme selection, registry callbacks, descriptor flags and additional paths remain symbolic',
                semantic_status='Reviewed D65E1B0/D65DF90 descriptor use and gate; URL grammar is a conditional parameter candidate')
            if ptr(raw,24):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,24),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name == "general_number_action":
            raw = memory.read(payload, 28)
            minimum, maximum = int.from_bytes(raw[4:8], "big"), int.from_bytes(raw[8:12], "big")
            row.update(semantic_role="number_parameter", descriptor_raw_hex=raw.hex(),
                       path_semantics="parameter",
                       parameter={"kind": "unsigned_number", "min": minimum, "max": maximum,
                                  "storage_offset": int.from_bytes(raw[:4], "big"),
                                  "flags_raw_hex": raw[24:28].hex()},
                       semantic_status="consumer-validated number bounds; flags not interpreted")
            help_ptr = ptr(raw, 16)
            if help_ptr:
                try:
                    row["help_candidate"] = read_cstring(memory, help_ptr, 512)
                except MemoryReadError as exc:
                    row["help_error"] = str(exc)
        elif name == "number_func_action":
            raw=memory.read(payload,24);callback=ptr(raw,8)
            row.update(semantic_role='number_parameter',path_semantics='parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'unsigned_number_dynamic' if callback else 'unsigned_number',
                    'storage_offset':int.from_bytes(raw[:4],'big'),'min':0,'max':0xffffffff,
                    'bounds_evaluated':not bool(callback),'bounds_callback':callback,
                    'default_bounds_only':bool(callback)},
                parameter_condition={'kind':'dynamic_number_bounds','callback':callback,'evaluated':False} if callback else None,
                parameter_gap='Numeric bounds callback has not been executed or fully resolved' if callback else None,
                semantic_status='Consumer-validated number parameter; dynamic bounds retained as unknown')
            if ptr(raw,16):
                try:row['help_candidate']=read_cstring(memory,ptr(raw,16),512)
                except MemoryReadError as exc:row['help_error']=str(exc)
        elif name == "interface_action":
            raw=memory.read(payload,60);flags=int.from_bytes(raw[16:20],'big')
            row.update(semantic_role='interface_parameter',path_semantics='parameter',descriptor_raw_hex=raw.hex(),
                parameter={'kind':'interface_type' if flags&0x80 else 'interface','storage_offset':int.from_bytes(raw[:4],'big'),
                    'flags_raw_hex':raw[16:20].hex(),'validation_callback':ptr(raw,48),'registry_selection_unresolved':True},
                parameter_condition={'kind':'interface_registry_and_validation','callback':ptr(raw,48),'flags_raw_hex':raw[16:20].hex(),'evaluated':False},
                parameter_gap='Interface registry/type/number validation and context effects remain unresolved',
                semantic_status='Consumer-validated interface argument; runtime type registry and validation retained')
        elif name == "char_action":
            raw=memory.read(payload,4);code=int.from_bytes(raw,'big')
            row.update(path_semantics='literal_character',semantic_role='literal_character',descriptor_raw_hex=raw.hex(),
                literal_character_code=code,literal_character=chr(code) if 32<=code<=126 else None,
                spacing_semantics='Consumes exactly the next input character; surrounding whitespace is not inferred',
                semantic_status='Consumer-validated exact next-character match; alternate consumes no character')
        elif name == "general_string_action":
            raw = memory.read(payload, 20)
            row.update(semantic_role="string_parameter", descriptor_raw_hex=raw.hex(),
                       path_semantics="parameter",
                       parameter={"kind": "string", "storage_offset": int.from_bytes(raw[:2], "big"),
                                  "size_candidate": int.from_bytes(raw[2:4], "big"),
                                  "flags_raw_hex": raw[16:20].hex()},
                       semantic_status="consumer-validated string descriptor; LINE/WORD flags unresolved")
            help_ptr = ptr(raw, 8)
            if help_ptr:
                try:
                    row["help_candidate"] = read_cstring(memory, help_ptr, 512)
                except MemoryReadError as exc:
                    row["help_error"] = str(exc)
        elif name == "generic_prefix_action":
            raw = memory.read(payload, 24)
            row.update(semantic_role="prefix_parameter", path_semantics="parameter", descriptor_raw_hex=raw.hex(),
                       parameter={"kind": "prefix_dynamic", "storage_offset": int.from_bytes(raw[:2], "big", signed=True),
                                  "prefix_length_storage_offset": int.from_bytes(raw[2:4], "big", signed=True),
                                  "address_type_candidate": int.from_bytes(raw[16:20], "big"),
                                  "flags_raw_hex": raw[20:24].hex(), "separator": "/",
                                  "address_registry_rva": 0x3cb56200},
                       parameter_condition={"kind": "registered_address_parser_and_prefix_length", "evaluated": False,
                                            "registry_rva": 0x3cb56200, "address_type_candidate": int.from_bytes(raw[16:20], "big")},
                       parameter_gap="Address-family registry, parser callback, prefix bound and input/context gates remain unresolved",
                       semantic_status="Reviewed E3A5E90 normal CLI descriptor and slash/length consumer; address family not inferred")
            if ptr(raw, 8):
                try:
                    row["help_candidate"] = read_cstring(memory, ptr(raw, 8), 512)
                except MemoryReadError as exc:
                    row["help_error"] = str(exc)
        elif name in ("generic_addr_action", "generic_addr_noflag_action"):
            raw = memory.read(payload, 24 if name == "generic_addr_action" else 20)
            row.update(semantic_role="address_parameter", path_semantics="parameter", descriptor_raw_hex=raw.hex(),
                       parameter={"kind": "address", "storage_offset": int.from_bytes(raw[:4], "big"),
                                  "address_type_candidate": int.from_bytes(raw[16:20], "big"),
                                  "flags_raw_hex": raw[20:24].hex() if len(raw) >= 24 else "00000000"},
                       semantic_status="consumer-validated address descriptor; address family and flags unresolved")
            if ptr(raw, 8):
                try:
                    row["help_candidate"] = read_cstring(memory, ptr(raw, 8), 512)
                except MemoryReadError as exc:
                    row["help_error"] = str(exc)
        elif name in ("params_action", "params_command_action"):
            raw = memory.read(payload, 76)
            row["descriptor_raw_hex"] = raw.hex()
            keyword = read_cstring(memory, ptr(raw), 96)
            if not re.fullmatch(r"[A-Za-z0-9_.:/+<>-]{1,80}", keyword):
                row["keyword_text_unparsed"] = keyword
                raise MemoryReadError("Combined parameter keyword is not a simple token")
            lower, upper = int.from_bytes(raw[12:16], "big"), int.from_bytes(raw[16:20], "big")
            row.update(semantic_role="combined_command_terminal", path_semantics="parameter_terminal",
                       keyword_candidate=keyword, keyword_address=ptr(raw), handler_candidate=ptr(raw, 24),
                       handler_field=payload + 24, handler_metadata=function(ptr(raw, 24)),
                       selector_candidate=int.from_bytes(raw[32:36], "big"),
                       parameter={"kind": "unsigned_number", "min": min(lower, upper), "max": max(lower, upper),
                                  "declared_bounds": [lower, upper], "storage_offset": int.from_bytes(raw[8:12], "big"),
                                  "flags_raw_hex": raw[64:68].hex()},
                       omit_parameter_when_negative=bool(int.from_bytes(raw[64:68], "big") & 8),
                       privilege_descriptor_raw_hex=raw[56:64].hex(), command_flags_raw_hex=raw[72:76].hex(),
                       semantic_status="consumer-validated keyword/number/EOL macro; privilege and numeric flags remain unresolved")
            for off, field in ((40, "help_candidate"), (48, "parameter_help_candidate")):
                if ptr(raw, off):
                    try:
                        row[field] = read_cstring(memory, ptr(raw, off), 512)
                    except MemoryReadError as exc:
                        row[field + "_error"] = str(exc)
        elif name.startswith('keyword_option') or name=='keyword_dynamic_option_func_action':
            from .option_tables import decode_options
            decode_options(memory,row,name,pointer_mode,image_base,option_models or {})
        elif name=='multiple_funcs_action':
            raw=memory.read(payload,32)
            row.update(path_semantics='branch_table',semantic_role='parser_ambiguity_branch',descriptor_raw_hex=raw.hex(),
                condition={'kind':'parser_ambiguity_or_remaining_input','evaluated':False,
                    'expression':'multiple_functions_check(csb) || remaining_input_check(csb)',
                    'context_fields':[0x3820,0x3A30,0x3AD8,0x2EB8,0x2FF8,0x3824,0x3A34,0x3534,0x2F5C],
                    'normal_cli_only':True},
                semantic_status='Consumer-validated alternate then descriptor +16/+24 branch; targets are transitions, not callback addresses')
            row['semantic_edges']=[{'target':ptr(raw,16),'kind':'multiple_functions_false','expected':False,'field_address':payload+16},
                                   {'target':ptr(raw,24),'kind':'multiple_functions_true','expected':True,'field_address':payload+24}]
        elif name=='test_func_action':
            raw=memory.read(payload,24)
            row.update(path_semantics='branch_table',semantic_role='no_argument_predicate',descriptor_raw_hex=raw.hex(),
                condition={'kind':'no_argument_predicate','callback':ptr(raw),'evaluated':False,'normal_cli_only':True},
                branch_effects=True,branch_gap='Predicate callback effects unresolved',
                effects=[{'kind':'parser_state_assignment','field_offset':9336,'width_candidate':4,'operation':'assign','value_raw_hex':'00000001'},
                         {'kind':'context_callback','function_candidate':ptr(raw),'no_arguments':True,'effects_unresolved':True}],
                semantic_status='Consumer-validated void-argument callback; +8 false/+16 true; callback never executed')
            row['semantic_edges']=[{'target':ptr(raw,8),'kind':'callback_false','expected':False,'field_address':payload+8},
                                   {'target':ptr(raw,16),'kind':'callback_true','expected':True,'field_address':payload+16}]
        elif name == "testexpr_action":
            raw = memory.read(payload, 24)
            predicate = ptr(raw, 16)
            row.update(semantic_role="predicate", descriptor_raw_hex=raw.hex(),
                       path_semantics="predicate",
                       condition={"predicate_candidate": predicate, "predicate_metadata": function(predicate),
                                  "false_target_candidate": ptr(raw, 8), "evaluated": False,
                                  "note": "Normal execution and help/NVGEN paths use different scheduling rules"},
                       semantic_status="consumer-validated predicate fields; never evaluated")
            row["semantic_edges"] = [{"target": ptr(raw, 8), "kind": "predicate_false_candidate",
                                      "field_address": payload + 8, "raw_hex": raw[8:16].hex()}]
        elif name == "test_action":
            raw = memory.read(payload, 48)
            row.update(semantic_role="comparison", path_semantics="comparison", descriptor_raw_hex=raw.hex(),
                       condition={"field_offset": int.from_bytes(raw[:2], "big"),
                                  "width_candidate": int.from_bytes(raw[2:4], "big"),
                                  "comparison_value_raw_hex": raw[8:16].hex(), "evaluated": False},
                       semantic_status="consumer-validated comparison branches; parser state not evaluated")
            row["semantic_edges"] = [{"target": ptr(raw, off), "kind": "comparison_" + relation,
                                      "field_address": payload + off, "raw_hex": raw[off:off + 8].hex()}
                                     for off, relation in ((16, "eq"), (24, "ne"), (32, "lt"), (40, "gt"))]
        elif name == 'set_string_action':
            raw=memory.read(payload,16);target=int.from_bytes(raw[:4],'big');source=ptr(raw,8)
            row.update(path_semantics='epsilon_accept',semantic_role='constant_string_assignment',descriptor_raw_hex=raw.hex(),
                effects=[{'kind':'constant_string_assignment','field_offset':target,'source_address':source,
                    'max_copied_bytes':254,'consumes_input':False,'value_resolved':False},
                    {'kind':'parser_state_assignment','field_offset':9336,'width_candidate':4,'value_raw_hex':'00000001','operation':'assign'}],
                semantic_status='Consumer-validated constant string copy and accept continuation; not a CLI token')
            try:
                row['effects'][0].update(value=read_cstring(memory,source,255),value_resolved=True)
            except MemoryReadError as exc:row['constant_string_error']=str(exc)
        elif name == 'set_decoder_action':
            raw=memory.read(payload,8)
            row.update(path_semantics='epsilon_accept',semantic_role='decoder_assignment',descriptor_raw_hex=raw.hex(),
                effects=[{'kind':'decoder_assignment','field_offset':9304,'decoder_address':ptr(raw),'consumes_input':False,'decoder_semantics_unresolved':True},
                         {'kind':'parser_state_assignment','field_offset':9336,'width_candidate':4,'value_raw_hex':'00000001','operation':'assign'}],
                semantic_status='Consumer-validated decoder pointer assignment and accept continuation; decoder not executed')
        elif name == 'iterator_action':
            raw=memory.read(payload,24)
            row.update(path_semantics='iterator',semantic_role='nvgen_iterator',descriptor_raw_hex=raw.hex(),
                iterator={'callback':ptr(raw),'field_offset':int.from_bytes(raw[8:12],'big'),'argument':ptr(raw,16),
                    'callback_only_when_nvgen':True,'callback_evaluated':False},
                semantic_status='Consumer-validated ordinary CLI: alternate and accept without token; NVGEN callback iteration unresolved')
        elif name in ("set_action", "orset_action"):
            raw = memory.read(payload, 16)
            row.update(path_semantics="epsilon_accept", semantic_role="state_assignment", descriptor_raw_hex=raw.hex(),
                       effects=[{"kind": "parser_state_assignment", "field_offset": int.from_bytes(raw[:4], "big"),
                                 "operation": "or" if name == "orset_action" else "assign",
                                 "width_candidate": int.from_bytes(raw[4:8], "big"),
                                 "value_raw_hex": raw[8:16].hex(), "evaluated": False}],
                       semantic_status="consumer-validated state assignment; symbolic value retained")
        elif name == "priv_action":
            raw = memory.read(payload, 16)
            row.update(path_semantics="branch_table", semantic_role="privilege_condition", descriptor_raw_hex=raw.hex(),
                       condition={"kind": "privilege_gate", "descriptor": ptr(raw), "evaluated": False},
                       semantic_status="consumer-validated privilege branch; privilege value not interpreted")
            row["semantic_edges"] = [{"target": ptr(raw, 8), "kind": "privilege_denied", "expected": False,
                                      "field_address": payload + 8, "raw_hex": raw[8:16].hex()}]
            row["conditional_accept"] = {"expected": True}
        elif name == "test_idbstatus_action":
            raw = memory.read(payload, 16)
            row.update(path_semantics="branch_table", semantic_role="interface_status_condition", descriptor_raw_hex=raw.hex(),
                       condition={"kind": "interface_status_mask", "mask_candidate": int.from_bytes(raw[8:12], "big"),
                                  "evaluated": False, "note": "Normal CLI requires a current interface/IDB; help paths differ"},
                       semantic_status="consumer-validated interface status branches; interface state not read")
            row["semantic_edges"] = [{"target": ptr(raw), "kind": "interface_status_zero", "expected": False,
                                      "field_address": payload, "raw_hex": raw[:8].hex()}]
            row["conditional_accept"] = {"expected": True}
        elif name == "test_boolean_action":
            raw = memory.read(payload, 24)
            row.update(path_semantics="branch_table", semantic_role="runtime_boolean_condition", descriptor_raw_hex=raw.hex(),
                       condition={"kind": "runtime_boolean", "variable_address": ptr(raw), "evaluated": False},
                       semantic_status="consumer-validated boolean targets; runtime variable not read")
            row["semantic_edges"] = [{"target": ptr(raw, off), "kind": "runtime_boolean_" + str(value).lower(),
                                      "expected": value, "field_address": payload + off, "raw_hex": raw[off:off + 8].hex()}
                                     for off, value in ((8, False), (16, True))]
        elif name == "func_action":
            raw = memory.read(payload, 12)
            row.update(path_semantics="epsilon_accept", semantic_role="context_callback", descriptor_raw_hex=raw.hex(),
                       effects=[{"kind": "context_callback", "function_candidate": ptr(raw),
                                 "function_metadata": function(ptr(raw)), "flags_raw_hex": raw[8:12].hex(),
                                 "evaluated": False, "effects_unresolved": True}],
                       semantic_status="consumer-validated callback and continuation; callback effects unresolved")
        elif name == "help_action":
            raw = memory.read(payload, 8)
            row.update(semantic_role="help", descriptor_raw_hex=raw.hex(),
                       semantic_status="consumer-validated alternate-only help node")
            if ptr(raw):
                row["help_candidate"] = read_cstring(memory, ptr(raw), 1024)
        elif name.startswith(("test_", "is_", "keyword_option_", "multiple_funcs")):
            row["semantic_role"] = "unresolved_condition_or_options"
    except MemoryReadError as exc:
        row["semantic_error"] = str(exc)


def summarize_graph(graph):
    nodes = graph["nodes"]
    return {"nodes": len(nodes), "edges": len(graph["edges"]),
            "keywords": sum("keyword_candidate" in row for row in nodes),
            "mapped_actions": sum("action_name" in row for row in nodes),
            "terminals": sum(row.get("semantic_role") in ("command_terminal", "combined_command_terminal") for row in nodes),
            "unique_handler_candidates": len({row["handler_candidate"] for row in nodes if row.get("handler_candidate")}),
            "parameters": sum(row.get("semantic_role") in ("number_parameter", "string_parameter", "address_parameter", "combined_command_terminal") for row in nodes),
            "unresolved_payload_nodes": sum(row.get("semantic_status") == "action registry mapped; payload semantics unresolved" for row in nodes),
            "semantic_errors": sum("semantic_error" in row for row in nodes),
            "runtime_action_nodes": sum(bool(row.get("action_function_requires_runtime")) for row in nodes),
            "unresolved_nodes": sum(row["status"] == "unresolved" for row in nodes)}


def node_title(row):
    role = row.get("semantic_role")
    if role in ('time_parameter','hex_parameter','url_parameter','signed_number_parameter','prefix_parameter'):
        from .syntax_paths import parameter_label
        return parameter_label(row['parameter'])
    if role == "command_terminal":
        handler = row.get("handler_candidate")
        return "<cr> -> " + (hex(handler) if handler else "unresolved handler")
    if role == "number_parameter":
        parameter = row["parameter"]
        if parameter.get('kind')=='unsigned_number_dynamic':return '<number:dynamic>'
        return "<number %d..%d>" % (parameter["min"], parameter["max"])
    if role=='interface_parameter':return '<interface-type>' if row['parameter']['kind']=='interface_type' else '<interface>'
    if role=='literal_character':return row.get('literal_character') or '<char:%#x>'%row['literal_character_code']
    if role == "string_parameter":
        return "<string>"
    if role == "address_parameter":
        return "<address>"
    if role == "combined_command_terminal":
        return row["keyword_candidate"] + " <number> <cr> -> " + hex(row["handler_candidate"])
    return row.get("keyword_candidate") or row.get("action_name") or "op_%s" % row.get("opcode", "?")
