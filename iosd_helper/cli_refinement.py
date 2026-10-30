"""Reinterpret reviewed CLI consumers while preserving the source graph and gaps."""
from copy import deepcopy
from .grammar_semantics import decode_action_payload,node_title


def refine_node(memory,source,profile,identity):
    if profile['input_md5'].lower()!=identity['input_md5'].lower():
        raise ValueError('CLI semantic profile belongs to a different image')
    name=source.get('action_name');review=profile['reviewed_actions'].get(name)
    if review is None:return None
    if review.get('refine_when')=='opaque_only' and source.get('path_semantics') and not source.get('semantic_error'):
        return None
    row=deepcopy(source);base=identity['imagebase']
    expected=base+int(review['function_rva'],0)
    observation=source.get('action_dispatch_observation',{})
    if source.get('action_function')!=expected or not observation.get('verified'):
        row['refinement_skipped']='Action dispatch differs from reviewed consumer or is unverified'
        return row
    # These fields belong to the previous interpretation. Raw bytes, dispatch,
    # provenance and unrelated uncertainty fields remain attached to the row.
    for key in ('semantic_error','path_semantics','semantic_role','keyword_text_unparsed'):
        row.pop(key,None)
    action={'name':name,'function':expected,'address':source['action_registry_entry']}
    decode_action_payload(memory,row,action,'swap_then_mask',image_base=base)
    reasons=set(source.get('remaining_uncertainties',[]))
    if row.get('path_semantics'):reasons.discard('action_semantics_unresolved')
    else:reasons.add('action_semantics_unresolved')
    if row.get('semantic_error'):reasons.add('descriptor_decode_error')
    else:reasons.discard('descriptor_decode_error')
    if row.get('parameter_gap'):reasons.add('parameter_validation_unresolved')
    if row.get('keyword_gap'):reasons.add('keyword_flags_or_access_unresolved')
    if row.get('help_error'):reasons.add('help_unread')
    if any(e.get('effects_unresolved') for e in row.get('effects',[])):reasons.add('state_operation_unresolved')
    row.update(remaining_uncertainties=sorted(reasons),display_label=node_title(row),
               refinement_scope='Reviewed consumer applied to saved exact pages; connected modes inherited from source')
    return row
