"""Verify saved NVGEN descriptor links and evidence identities, not target behavior."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    cli=argparse.ArgumentParser(description=__doc__);cli.add_argument('analysis')
    args=cli.parse_args();folder=Path(args.analysis)
    summary=json.loads((folder/'binding-summary.json').read_text(encoding='utf-8'))
    expected=summary['identity']['input_md5'];base=summary['identity']['imagebase']
    functions={};hashes={}
    for path in folder.rglob('rva_*.json'):
        record=json.loads(path.read_text(encoding='utf-8'))
        assert record['input_md5']==expected
        assert record['base']==base
        functions[record['rva']]=str(path.relative_to(folder))
        hashes[str(path.relative_to(folder))]=hashlib.sha256(path.read_bytes()).hexdigest()
    required=(0xe0de210,0xe39d8f0,0xe39d9b0,0xe0e6a00,0xe400e90,0xdef9650,0xdef9790,
              0xe3fc690,0xe406010,0xe3fc1b0,0xe0d5e90,0xdf331e0,0xdf2d060,0xdf34330)
    assert all(rva in functions for rva in required)
    nodes={}
    for name in ('special-parser-nodes.json','disable-cache-root.json','disable-cache-leaf.json'):
        path=folder/name;capture=json.loads(path.read_text(encoding='utf-8'))
        assert capture['input_md5']==expected and capture['base']==base
        hashes[name]=hashlib.sha256(path.read_bytes()).hexdigest()
        for row in capture['rows']:
            assert row['mask_hex']=='ffffffffff'
            assert row.get('payload_mask_hex')=='ffffffffffffffff'
            nodes[row['rva']]=row
    ptr=lambda raw,offset:int.from_bytes(raw[offset:offset+8],'big') & 0x7fffffffffffffff
    raw=bytes.fromhex(nodes[0x340a86a0]['payload_raw_hex'])
    assert int.from_bytes(raw[:2],'big')==9636 and int.from_bytes(raw[8:16],'big')==1
    assert ptr(raw,16)==base+0x340a9098
    iterator=nodes[0x340a9098]
    assert iterator['opcode_be']==68 and iterator['links_va'][0]==base+0x340a90e8
    assert ptr(bytes.fromhex(iterator['payload_raw_hex']),0)==base+0xdf2d060
    free=nodes[0x340a90e8]
    assert free['opcode_be']==28 and ptr(bytes.fromhex(free['payload_raw_hex']),0)==base+0xdf34330
    for rva in (0x342be680,0x342be950):
        raw=bytes.fromhex(nodes[rva]['payload_raw_hex'])
        assert nodes[rva]['opcode_be']==28
        assert ptr(raw,0)==base+0xe3fc1b0 and int.from_bytes(raw[8:12],'big')==4
    for rva,callback,selector in ((0x34149120,0xe40c850,3),(0x340bc398,0xdef9650,0)):
        raw=bytes.fromhex(nodes[rva]['payload_raw_hex'])
        assert ptr(raw,0)==base+callback and int.from_bytes(raw[8:12],'big')==selector
    cases=json.loads((folder/'case-associations.json').read_text(encoding='utf-8'))
    assert any(c['callback_rva']==0xe0e6a00 and c['selector']==0 and any(e['node']==base+0x34148098 for e in c['same_function_and_selector_matches']) for c in cases)
    assert any(c['callback_rva']==0xe40c850 and c['selector']==3 and any(e['node']==base+0x34149120 for e in c['same_function_and_selector_matches']) for c in cases)
    associations=[json.loads(line) for line in (folder/'cli-nvgen-associations.jsonl').open(encoding='utf-8')]
    assert len(associations)==summary['nvgen_nodes']
    assert sum(bool(r['same_function_and_selector_matches']) for r in associations)==summary['nvgen_nodes_sharing_cli_function_and_selector']
    result={'input_md5':expected,'capture_base':base,'collected_idb_functions':len(functions),
            'saved_descriptor_links_verified':True,'documented_handler_pairs_verified':True,
            'target_callbacks_executed':False,'live_cache_enable_state_read':False,
            'all_invalidation_triggers_recovered':False,'source_sha256':hashes,
            'scope':'Saved bytes, identities and associations only; callback behavior is a reviewed interpretation, not an execution test'}
    (folder/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'}))


if __name__=='__main__':main()
