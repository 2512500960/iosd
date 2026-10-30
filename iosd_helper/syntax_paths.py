"""Mode-scoped syntax witnesses with explicit token consumption and provenance.

This is a bounded symbolic interpretation of reviewed normal-CLI operations,
not an emulator. It never calls target predicates/handlers or edits the IDB.
"""
from collections import Counter, defaultdict
import heapq
from itertools import count


TRACKED_FIELDS = (9328, 9332, 9636)  # sense, default, NVGEN; pinned sample only


def number(value):
    return int(value, 0) if isinstance(value, str) else int(value)


def raw_links(node):
    raw = bytes.fromhex(node.get("raw_hex", ""))
    return ([int.from_bytes(raw[:8], "little"), int.from_bytes(raw[8:16], "little")]
            if len(raw) >= 16 else [0, 0])


def flatten_conditions(conditions):
    for condition in conditions:
        if condition.get('kind')=='keyword_constraints':
            yield from flatten_conditions(condition['constraints'])
        else:yield condition


def parameter_label(parameter):
    kind=parameter.get('kind')
    if kind=='unsigned_number':return '<number:%s..%s>'%(parameter['min'],parameter['max'])
    if kind=='signed_number':return '<signed:%s..%s>'%(parameter['min'],parameter['max'])
    return {'unsigned_number_dynamic':'<number:dynamic>','address':'<address>','string':'<string>',
            'interface':'<interface>','interface_type':'<interface-type>',
            'prefix_dynamic':'<prefix:dynamic>','time_hm':'<hh:mm>','time_hms':'<hh:mm:ss>',
            'hexstring':'<hex-string>','hexdata':'<hex-data>','url_dynamic':'<url:dynamic>'}.get(kind,'<parameter:unresolved>')


def registration_overlays(graph, nodes):
    """Represent possible installations as additional edges, without ordering them.

    DEF70B0 appends type-1 registrations to the slot's alternate chain. We expose
    them as alternatives at that chain's head, retaining each call's conditions.
    Type-2 bindings are only modeled when the observed sentinel precondition holds.
    """
    slots = defaultdict(list)
    for slot in graph.get("link_registry", []) + graph.get("dynamic_link_definitions", []):
        slots[slot["key"]].append(slot)
    overlays, unmatched, rejected = defaultdict(list), [], []
    for index, registration in enumerate(graph.get("registrations", [])):
        candidates = slots.get(registration["link_key"])
        if not candidates:
            unmatched.append(index)
            continue
        accepted = False
        for slot in candidates:
            source, target = slot["root"], registration["root"]
            if slot["type"] == 2:
                source, target = target, source
                if raw_links(nodes.get(source, {}))[1] != 0x3CB665C8:
                    continue
            accepted = True
            overlays[source].append({"target": target, "kind": "candidate_registration_installation",
                                 "registration_index": index, "slot_address": slot["address"],
                                 "slot_type": slot["type"], "key": slot["key"],
                                 "slot_definition": slot,
                                 "note": "Static candidate; slot creation, caller conditions and installation order unresolved"})
        if not accepted:
            rejected.append(index)
    return dict(overlays), unmatched, rejected


def state_after(node, state, profile):
    state = list(state)
    for effect in node.get("effects", []):
        if effect.get('effects_unresolved') and effect.get('storage_offset_candidate') in TRACKED_FIELDS:
            state[TRACKED_FIELDS.index(effect['storage_offset_candidate'])]=None
            continue
        offset = effect.get("field_offset")
        if offset in TRACKED_FIELDS:
            value = int(effect.get("value_raw_hex") or "0", 16)
            if effect.get("operation") == "or":
                old = state[TRACKED_FIELDS.index(offset)]
                value = (old | value) if old is not None else (1 if value == 1 else None)
            state[TRACKED_FIELDS.index(offset)] = value if value in (0, 1) else None
        elif effect.get("kind") == "context_callback":
            reviewed = {number(ea) for ea in profile.get("reviewed_normal_cli_callbacks", [])}
            if effect.get("function_candidate") not in reviewed:
                state[0] = state[1] = None
    return tuple(state)


def semantic_options(node, state, graph):
    """Each returned edge says exactly which text/state applies to that branch."""
    accept, alternate = raw_links(node)
    kind = node.get("path_semantics")
    options = []
    def add(target, branch, token=None, condition=None, effects=False, gap=None):
        if target:
            edge = {"target": target, "kind": branch}
            if token is not None:
                edge["token"] = token
            if condition is not None:
                edge["condition"] = {"node": node["address"], **condition}
            if effects:
                edge["apply_effects"] = True
            if gap:
                edge["gap"] = gap
            options.append(edge)
    if node.get("semantic_error") or node.get('dispatch_semantics_unverified'):
        kind = None
    if kind == "keyword":
        gates=node.get("keyword_access_gates")
        constraints=[]
        constraints.extend(node.get('keyword_extra_conditions',[]))
        if gates:constraints.append({"kind":"keyword_access_gates","gates":gates,"snapshot_only":True,
                       "evaluated":all(g.get('evaluated') for g in gates)})
        pre=node.get('keyword_state_precondition');allowed=True
        if pre:
            offset=pre['field_offset'];known=state[TRACKED_FIELDS.index(offset)] if offset in TRACKED_FIELDS else None
            mask=int(pre['mask_raw_hex'],16)
            allowed=known is None or known&mask==0
            constraints.append({**pre,'evaluated':known is not None,'known_value':known,'required':'value & mask == 0'})
        condition=constraints[0] if len(constraints)==1 else ({'kind':'keyword_constraints','constraints':constraints} if constraints else None)
        if allowed:add(accept,"keyword_match",node['keyword_candidate'],effects=True,condition=condition,gap=node.get('keyword_gap'))
        add(alternate, "keyword_alternative")
    elif kind=='keyword_options':
        wrapper=node.get('option_wrapper_condition')
        add(alternate,'option_alternative',condition=wrapper)
        for index,item in enumerate(node.get('keyword_options',[])):
            if item.get('keyword_unparsed'):continue
            constraints=list(item.get('conditions',[]));allowed=True
            if wrapper:constraints.append(wrapper)
            gates=node.get('keyword_access_gates')
            if gates:constraints.append({'kind':'keyword_access_gates','gates':gates,'snapshot_only':True,'evaluated':all(g.get('evaluated') for g in gates)})
            pre=item.get('state_precondition')
            if pre:
                offset=pre['field_offset'];known=state[TRACKED_FIELDS.index(offset)] if offset in TRACKED_FIELDS else None
                allowed=known is None or known&int(pre['mask_raw_hex'],16)==0
                constraints.append({**pre,'known_value':known,'evaluated':known is not None})
            if not allowed:continue
            constraints.append({'kind':'keyword_option_match','minimum_match':item.get('minimum_match',0),
                'value':item['value'],'evaluated':False,'note':'Privilege, parser mode, ambiguity and additional flags still constrain matching'})
            count_before=len(options)
            add(accept,'keyword_option_match',item['keyword'],condition={'kind':'keyword_constraints','constraints':constraints})
            if len(options)>count_before:
                options[-1].update(option_index=index,option_effects=item.get('effects',[]))
        if not node.get('option_enumeration_complete') or node.get('option_frontiers'):
            add(accept,'unresolved_option_match','<?option@%x>'%node['address'],condition={'kind':'unresolved_option_source',
                'source':node.get('option_source'),'frontiers':node.get('option_frontiers',[]),'evaluated':False},gap='Additional option producer entries or table fragments unresolved')
    elif kind == "parameter":
        parameter = node.get("parameter", {})
        label=parameter_label(parameter)
        add(accept, "parameter_match", label, effects=True,condition=node.get('parameter_condition'),gap=node.get('parameter_gap'))
        add(alternate, "parameter_alternative")
    elif kind == 'whitespace':
        add(alternate, 'whitespace_alternative')
        if state[2] != 1:
            add(accept, 'whitespace_input_match', condition={"kind": "whitespace_or_input_boundary",
                **node.get('whitespace', {}), "expected_nvgen": 0, "evaluated": False},
                gap='Input characters, separator length and boundary context have not been evaluated')
        if state[2] != 0:
            add(accept, 'whitespace_nvgen_bypass', condition={"kind": "whitespace_nvgen_gate",
                "expected_nvgen": 1, "evaluated": state[2] == 1})
    elif kind=='literal_character':
        token=node.get('literal_character') or '<char:%#x>'%node['literal_character_code']
        add(accept,'literal_character_match',token,condition={'kind':'exact_input_character','code':node['literal_character_code'],
            'surrounding_whitespace_inferred':False,'evaluated':False})
        add(alternate,'literal_character_alternative')
    elif kind=='iterator':
        add(alternate,'iterator_alternative')
        nvgen=state[2]
        if nvgen!=1:add(accept,'iterator_normal_cli',condition={'kind':'iterator_nvgen_gate','expected_nvgen':0,'evaluated':nvgen==0})
        if nvgen!=0:add(accept,'iterator_nvgen_iteration',condition={'kind':'iterator_nvgen_gate','expected_nvgen':1,
            'callback':node['iterator']['callback'],'evaluated':False},gap='NVGEN iterator callback and generated objects unresolved')
    elif kind in ("epsilon_both", "epsilon_links"):
        add(accept, "control_accept")
        add(alternate, "control_alternate")
        if kind == "epsilon_links":
            for edge in node.get("semantic_edges", []):
                if edge["kind"] == "link_extra_candidate":
                    add(edge["target"], "static_link_extra")
    elif kind == "epsilon_accept":
        decoder=any(e.get('decoder_semantics_unresolved') for e in node.get('effects',[]))
        add(accept, "control_accept", effects=True,gap='Assigned decoder semantics unresolved' if decoder else None)
    elif kind == "epsilon_alternate":
        add(alternate, "control_alternate")
    elif kind == "predicate":
        condition = node.get("condition", {})
        common = {"kind": "predicate", "function": condition.get("predicate_candidate"),
                  "function_name": (condition.get("predicate_metadata") or {}).get("name", ""), "evaluated": False}
        add(alternate, "predicate_alternative")
        add(accept, "predicate_true", condition={**common, "expected": True})
        add(condition.get("false_target_candidate"), "predicate_false", condition={**common, "expected": False})
    elif kind == "comparison":
        add(alternate, "comparison_alternative")
        condition = node.get("condition", {})
        offset = condition.get("field_offset")
        known = state[TRACKED_FIELDS.index(offset)] if offset in TRACKED_FIELDS else None
        value = int(condition.get("comparison_value_raw_hex") or "0", 16)
        for edge in node.get("semantic_edges", []):
            relation = edge["kind"][len("comparison_"):]
            result = None if known is None else {"eq": known == value, "ne": known != value,
                                                "lt": known < value, "gt": known > value}.get(relation)
            if result is not False:
                add(edge["target"], edge["kind"], condition={"kind": "parser_state_comparison", **condition,
                    "relation": relation, "evaluated": result is not None,
                    "evaluation_source": "symbolic local state" if result is not None else "unresolved"})
    elif kind == "branch_table":
        add(alternate, "condition_alternative")
        common = node.get("condition", {})
        if node.get("conditional_accept"):
            add(accept, "condition_accept", condition={**common, **node["conditional_accept"]})
        for edge in node.get("semantic_edges", []):
            add(edge["target"], edge["kind"], condition={**common, "expected": edge["expected"]},
                effects=node.get('branch_effects',False),gap=node.get('branch_gap'))
    elif kind == "parameter_terminal":
        add(alternate, "combined_keyword_alternative")
    elif kind == "sense_choice":
        sense, default, nvgen = state
        positive = True if nvgen == 1 or (sense == 1 and default == 0) else (
            False if nvgen == 0 and (sense == 0 or default == 1) else None)
        common = {"kind": "normal_cli_noprefix", "state": list(state), "evaluated": positive is not None}
        if positive is not False:
            add(accept, "positive_parameter_path", condition={**common, "expected_positive": True})
        if positive is not True:
            add(alternate, "no_or_default_path", condition={**common, "expected_positive": False})
    elif kind in ("terminal", "stop"):
        pass
    elif node.get("status") == "transition_candidate":
        marker = "<?%s@%x>" % (node.get("action_name", "unknown_action"), node["address"])
        add(accept, "unresolved_accept", marker, gap="Action token/state/branch semantics unresolved")
        add(alternate, "unresolved_alternate", marker, gap="Action token/state/branch semantics unresolved")
    return options


def recover_mode(graph, definition, overlays, max_states, max_paths, cancelled, record_sink=None):
    nodes = {node["address"]: node for node in graph["nodes"]}
    settings = graph.get("path_analysis", {})
    initial = tuple(settings.get("initial_normal_cli_state", [1, 0, 0]))
    root = number(definition["root"])
    first = (root, initial)
    distances, previous = {first: (0, 0, 0)}, {}
    serial = count()
    heap = [(0, 0, 0, next(serial), first)]
    terminals, frontiers, settled = [], [], set()
    frontier_count = 0
    stop = "exhausted_modeled_states"
    while heap:
        unknowns, token_count, hops, _, key = heapq.heappop(heap)
        if key in settled or distances[key] != (unknowns, token_count, hops):
            continue
        if len(settled) >= max_states:
            stop = "state_limit"
            break
        if len(settled) % 1024 == 0 and cancelled():
            stop = "cancelled"
            break
        settled.add(key)
        ea, state = key
        node = nodes.get(ea)
        if not node or node.get("status") == "unresolved":
            frontier_count += 1
            if len(frontiers) < 1000:
                frontiers.append({"address": ea, "reason": (node or {}).get("reason", "Target absent from acquired graph")})
            continue
        if node.get("path_semantics") in ("terminal", "parameter_terminal") and not node.get("semantic_error"):
            terminals.append(key)
            if len(terminals) >= max_paths:
                stop = "path_limit"
                break
            if node.get("path_semantics") == "terminal":
                continue
        options = semantic_options(node, state, graph) + overlays.get(ea, [])
        for edge in options:
            next_state = state_after(node, state, settings) if edge.get("apply_effects") else state
            if edge.get('option_effects'):next_state=state_after({'effects':edge['option_effects']},next_state,settings)
            gap = edge.get("gap")
            if gap:
                next_state = (None, None, state[2])
            callback_gap = False
            if edge.get("apply_effects"):
                reviewed = {number(x) for x in settings.get("reviewed_normal_cli_callbacks", [])}
                callback_gap = any(effect.get("kind") == "context_callback" and effect.get("function_candidate") not in reviewed
                                   for effect in node.get("effects", []))
            next_key = (edge["target"], next_state)
            cost = (unknowns + bool(gap) + callback_gap, token_count + ("token" in edge), hops + 1)
            if next_key not in distances or cost < distances[next_key]:
                distances[next_key] = cost
                previous[next_key] = (key, {"source": ea, **edge})
                heapq.heappush(heap, (*cost, next(serial), next_key))
    pending_states=len(distances)-len(settled)
    if stop!='exhausted_modeled_states':
        for pending_key in distances:
            if pending_key in settled:continue
            frontier_count+=1
            if len(frontiers)<1000:
                frontiers.append({'address':pending_key[0],'tracked_state':list(pending_key[1]),'reason':stop})
    records = [];witness_count=0;unique_eols=set();unique_handlers=set();without_gaps=0
    for terminal in terminals:
        trace, chain, key = [], [], terminal
        while key != first:
            chain.append(key)
            key, edge = previous[key]
            trace.append(edge)
        chain.append(first)
        trace.reverse()
        chain.reverse()
        tokens, parameters, conditions, effects, gaps, registrations = [], [], [], [], [], []
        for edge in trace:
            node = nodes[edge["source"]]
            if "token" in edge:
                tokens.append(edge["token"])
            if edge["kind"] == "parameter_match":
                parameters.append({"node": node["address"], **node.get("parameter", {}), "help": node.get("help_candidate", "")})
            if edge.get("condition"):
                conditions.append(edge["condition"])
            if edge.get("apply_effects"):
                effects.extend({"node": node["address"], **effect} for effect in node.get("effects", []))
                reviewed = {number(x) for x in settings.get("reviewed_normal_cli_callbacks", [])}
                for effect in node.get("effects", []):
                    if effect.get("kind") == "context_callback" and effect.get("function_candidate") not in reviewed:
                        gaps.append({"node": node["address"], "reason": "Context callback effects unresolved", "function": effect.get("function_candidate")})
            if edge.get('option_effects'):effects.extend({'node':node['address'],'option_index':edge.get('option_index'),**effect} for effect in edge['option_effects'])
            if edge.get("gap"):
                gaps.append({"node": node["address"], "action": node.get("action_name"), "reason": edge["gap"]})
            if "registration_index" in edge:
                registration = graph["registrations"][edge["registration_index"]]
                registrations.append({"slot": edge["slot_address"], "slot_definition": edge.get("slot_definition"),
                                      "key": edge["key"], **registration})
        terminal_node = nodes[terminal[0]]
        if terminal_node.get("path_semantics") == "parameter_terminal":
            tokens.append(terminal_node["keyword_candidate"])
            omit = terminal_node.get("omit_parameter_when_negative") and terminal[1][0] == 0
            if not omit:
                parameter = terminal_node["parameter"]
                tokens.append("<number:%s..%s>" % (parameter["min"], parameter["max"]))
                parameters.append({"node": terminal[0], **parameter,
                                   "help": terminal_node.get("parameter_help_candidate", "")})
            conditions.append({"node": terminal[0], "kind": "combined_keyword_parameter_terminal",
                               "parameter_omitted": bool(omit), "sense": terminal[1][0],
                               "evaluated": terminal[1][0] is not None})
            if terminal[1][0] is None and terminal_node.get("omit_parameter_when_negative"):
                gaps.append({"node": terminal[0], "reason": "Parameter omission depends on unresolved sense state"})
        tokens.append("<cr>")
        record={"mode": definition["name"], "prompt": definition["prompt"], "mode_root": root,
                        "mode_evidence_call": definition.get("evidence_call"),
                        "syntax_candidate": " ".join(tokens), "parameters": parameters,
                        "conditions": conditions, "state_effects": effects,
                        "handler": terminal_node["handler_candidate"], "handler_metadata": terminal_node.get("handler_metadata"),
                        "eol_node": terminal[0], "selector_candidate": terminal_node.get("selector_candidate"),
                        "final_tracked_state": list(terminal[1]), "registration_candidates": registrations,
                        "node_addresses": [entry[0] for entry in chain], "edge_trace": trace,
                        "gaps": gaps, "syntax_status": "partial_syntax_candidate" if gaps else "syntax_candidate",
                        "availability": "runtime registration, privilege and predicate gates unverified"}
        witness_count+=1;unique_eols.add(record['eol_node']);unique_handlers.add(record['handler']);without_gaps+=not gaps
        if record_sink is None:records.append(record)
        else:record_sink(record)
    summary = {"mode": definition["name"], "prompt": definition["prompt"], "root": root,
               "settled_states": len(settled), "discovered_states": len(distances),
               "stop_reason": stop, "witnesses": witness_count,
               "unique_eols": len(unique_eols),
               "unique_handlers": len(unique_handlers),
               "syntax_candidates_without_opaque_steps": without_gaps,
               "frontier_states": frontier_count, "frontier_list_truncated": frontier_count > len(frontiers),
               "pending_modeled_states":pending_states,
               "frontiers": frontiers}
    return summary, records


def recover_paths(graph, mode_names=("configure", "interface"), max_states_per_mode=250000,
                  max_paths=30000, cancelled=lambda: False, record_sink=None):
    if not 1 <= max_states_per_mode <= 1000000 or not 1 <= max_paths <= 200000:
        raise ValueError("Invalid syntax recovery bounds")
    if graph.get("link_registry_errors"):
        raise ValueError("Static link registry is incomplete; inspect its errors first")
    nodes = {node["address"]: node for node in graph["nodes"]}
    overlays, unmatched, rejected = registration_overlays(graph, nodes)
    definitions = [mode for mode in graph.get("mode_definitions", []) if mode["name"] in mode_names]
    missing = set(mode_names) - {mode["name"] for mode in definitions}
    if missing:
        raise ValueError("Mode definitions missing: " + ", ".join(sorted(missing)))
    records, summaries = [], [];witness_total=0;handlers=set()
    def emit(record):
        handlers.add(record['handler'])
        if record_sink is None:records.append(record)
        else:record_sink(record)
    for definition in definitions:
        if witness_total >= max_paths or cancelled():
            break
        summary, paths = recover_mode(graph, definition, overlays, max_states_per_mode,
                                       max_paths - witness_total, cancelled, emit)
        summaries.append(summary)
        witness_total+=summary['witnesses']
        if summary["stop_reason"] == "cancelled":
            break
    summary = {"scope": "Witness per EOL/context, preferring fewer opaque steps then fewer tokens then fewer edges; not exhaustive syntax enumeration",
               "modes": summaries, "paths": witness_total, "unique_handlers": len(handlers),
               "mode_roots": graph.get("mode_definitions", []), "mode_evidence": graph.get("mode_evidence", {}),
               "requested_modes": list(mode_names), "unprocessed_modes": sorted(set(mode_names) - {s["mode"] for s in summaries}),
               "registration_overlay_edges": sum(map(len, overlays.values())),
               "registrations_without_static_slot": [graph["registrations"][i] for i in unmatched],
               "type2_precondition_failures": [graph["registrations"][i] for i in rejected],
               "limits": {"max_states_per_mode": max_states_per_mode, "max_paths": max_paths},
               "tracked_fields": dict(zip(map(str, TRACKED_FIELDS), ("sense", "default", "nvgen"))),
               "initial_state_assumption": graph.get("path_analysis", {}).get("initial_normal_cli_state", [1, 0, 0]),
               "runtime_conditions_evaluated": False,
               "records_streamed":record_sink is not None,
               "notes": ["Candidate registration edges overapproximate possible installation, not boot order or device availability.",
                         "Only local constant assignments to sense/default/NVGEN are tracked; other state remains symbolic.",
                         "Unknown actions are explicit opaque tokens; callback effects can make a path partial.",
                         "String/number flags and privilege descriptors remain unresolved even on paths without opaque steps."]}
    return {"summary": summary, "paths": records}
