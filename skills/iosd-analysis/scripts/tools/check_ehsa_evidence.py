"""Verify EHSA evidence identities, table links, retained gaps and GOT range matches."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from build_ehsa_report import MD5, decode


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('analysis',type=Path)
    folder=parser.parse_args().analysis.resolve()
    read=lambda p:json.loads(p.read_text(encoding='utf-8'))
    summary=read(folder/'summary.json');capture=read(folder/'fsm-tables.json')
    assert summary['input_md5']==MD5 and summary['capture_base']==capture['base']
    cells=read(folder/'fsm-cells.json');assert cells==decode(capture)
    assert len(cells)==224 and sum(r['state_name'] is None for r in cells)==16
    assert sum(r['callback_rva'] is not None for r in cells)==47
    assert sum(r['next_semantics']=='explicit_state' for r in cells)==41
    assert sum(r['next_semantics']=='keep_state' for r in cells)==183
    assert len({r['callback_rva'] for r in cells if r['callback_rva'] is not None})==19
    index={(r['state'],r['major'],r['minor']):r for r in cells}
    for state,event,nxt,cb in ((2,(1,0),3,0xd51b190),(3,(1,1),4,0xd51b1f0),
                               (4,(1,2),5,0xd51b2d0),(8,(1,5),9,0xd51b680),
                               (9,(1,6),10,0xd51ba00),(10,(1,7),11,0xd51bce0),
                               (11,(1,8),12,0xd51be10)):
        row=index[(state,*event)];assert row['next_state']==nxt and row['callback_rva']==cb
    for state in range(1,8):
        assert index[(state,2,0)]['callback_rva']==0xd51af30
    for row in summary['function_evidence']:
        path=folder/row['source'];assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
        saved=read(path);assert saved['input_md5']==MD5 and saved['base']==capture['base']
    got=summary['runtime_got_bindings']
    assert got['target_execution_changed'] is False and got['atomic_snapshot'] is False
    assert got['process_state_before']==got['process_state_after']
    expected={'cyan_get_boolean':'libcyan.so','chasfs_initialize':'libchasfs.so',
              'chasfs_property_get_string':'libchasfs.so','chasfs_property_present':'libchasfs.so',
              'chasfs_property_create':'libchasfs.so','__be_mcp_get_failover_reason':'libiosd_crb_vxe_unix.so',
              '__be_mcp_stop_nplusm_b2b_fd':'libiosd_crb_vxe_unix.so'}
    for row in got['rows']:
        raw=bytes.fromhex(row['raw_hex']);assert len(raw)==8
        value=int.from_bytes(raw,'little');assert value==row['pointer_va']
        assert row['status']=='module_range_match' and len(row['module_matches'])==1
        m=row['module_matches'][0]
        assert m['base']<=value<m['base']+m['size'] and value-m['base']==m['offset']
        assert m['name'].split('/')[-1]==expected[row['symbol']]
    html=BeautifulSoup((folder/'index.html').read_text(encoding='utf-8'),'html.parser')
    assert len(html.select('#fsm tbody tr'))==224
    for link in html.select('a[href]'):
        parsed=urlsplit(link['href'])
        if parsed.scheme or parsed.netloc or not parsed.path:continue
        assert (folder/unquote(parsed.path)).resolve().is_file(),link['href']
    assert len(summary['unknowns'])>=10 and not summary['all_state_reachability_proved']
    result={'input_md5':MD5,'saved_functions':summary['saved_functions'],'complete_event_cells':224,
            'action_callbacks':19,'got_range_matches':7,'saved_evidence_verified':True,
            'runtime_reachability_proved':False,'target_execution_tested':False,
            'scope':'Saved byte links, identities, hashes and module range arithmetic; not an execution or failover test'}
    (folder/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
