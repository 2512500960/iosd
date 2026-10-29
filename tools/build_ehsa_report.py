"""Build a sample-bound EHSA evidence report from saved captures, without IDA."""
import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re

from markdown_it import MarkdownIt

MD5 = '9eccfd46caadfff9c18557e2a446e19b'
STATE_NAMES = {
    1: 'REDUNDANCY_SYSTEM_START', 2: 'REDUNDANCY_WAIT_ACTIVE_RESTART_ACK',
    3: 'REDUNDANCY_WAIT_ACTIVE_BOOTACK', 4: 'REDUNDANCY_WAIT_ACTIVE_INITEDACK',
    5: 'REDUNDANCY_WAIT_STDBY_EHSA_ISSU_VERSIONING', 6: 'REDUNDANCY_WAIT_SWITCHOVER',
    7: None, 8: 'REDUNDANCY_PEERSTANDBY_NONOPERATIONAL',
    9: 'REDUNDANCY_PEERSTANDBY_DETECTED', 10: 'REDUNDANCY_PEERSTANDBY_INITWAIT',
    11: 'REDUNDANCY_EHSA_ISSU_VERSIONING', 12: 'REDUNDANCY_PEERSTANDBY_INITED',
    13: 'REDUNDANCY_PEERSTANDBY_NOTPRESENT', 14: 'ACTIVE_DONOT_RESPOND',
}
EVENT_NAMES = {
    0: 'FSM timer (0,0)', 1: 'RESTART ACK receive (1,0)',
    2: 'BOOT ACK receive (1,1)', 3: 'INITED ACK receive (1,2)',
    6: 'RESTART receive (1,5)', 7: 'BOOT receive (1,6)',
    8: 'INITED receive (1,7)', 10: 'transition error producer (1,9)',
    11: 'filtered peer state 0 (2,0)', 12: 'filtered peer state 1 (2,1)',
    14: 'filtered peer state 3 (2,3)',
}


def decode(capture):
    """Retain every event cell, including null callbacks and unresolved labels."""
    assert capture['input_md5'] == MD5
    assert capture['state_count'] == 14 and capture['entry_size'] == 24 and capture['event_count'] == 16
    base = capture['base']; result = []
    assert [s['state'] for s in capture['states']] == list(range(1, 15))
    for state in capture['states']:
        raw = bytes.fromhex(state['raw_hex'])
        assert len(raw) == 384 and bytes.fromhex(state['mask_hex']) == b'\xff' * 48
        descriptor = bytes.fromhex(state['descriptor_raw_hex'])
        assert bytes.fromhex(state['descriptor_mask_hex']) == b'\xff\xff'
        assert int.from_bytes(descriptor[:8], 'big') & 0x7fffffffffffffff == base + state['rva']
        assert int.from_bytes(descriptor[8:16], 'big') & 0x7fffffffffffffff == base + 0xd51aea0
        for event in range(16):
            cell = raw[event*24:(event+1)*24]
            cb = int.from_bytes(cell[:8], 'big') & 0x7fffffffffffffff
            nxt = int.from_bytes(cell[16:20], 'big', signed=True)
            major, minor = ((0, 0) if event == 0 else (1, event-1) if event <= 10 else (2, event-11))
            result.append({
                'state': state['state'], 'state_name': STATE_NAMES[state['state']],
                'cell_rva': state['rva'] + event*24, 'event_index': event,
                'major': major, 'minor': minor, 'event_name': EVENT_NAMES.get(event),
                'callback_rva': cb-base if cb else None, 'argument_raw_hex': cell[8:16].hex(),
                'next_state_raw': nxt,
                'next_state': nxt if 1 <= nxt <= 14 else state['state'] if nxt in (0, -2) else None,
                'next_semantics': 'explicit_state' if 1 <= nxt <= 14 else
                    'keep_state' if nxt == 0 else 'special_keep_state' if nxt == -2 else
                    'error' if nxt == -1 else 'unresolved',
                'raw_hex': cell.hex(),
                'unknowns': (['state_name'] if STATE_NAMES[state['state']] is None else []) +
                    (['event_producer_or_label'] if event not in EVENT_NAMES else []),
                'scope': 'Table-directed possibility, not runtime reachability or action success',
            })
    return result


def build(folder, root):
    load = lambda p: json.loads(p.read_text(encoding='utf-8'))
    capture = load(folder/'fsm-tables.json'); base = capture['base']
    cells = decode(capture)
    functions = {}
    for path in sorted(folder.rglob('rva_*.json')):
        row = load(path)
        assert row['input_md5'] == MD5 and row['base'] == base
        rva = row['rva']
        functions[rva] = {'rva': rva, 'size': row['size'],
                          'source': path.relative_to(folder).as_posix(),
                          'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    callbacks = {r['callback_rva'] for r in cells if r['callback_rva'] is not None}
    assert callbacks <= set(functions)
    architecture = load(root/'reports/iosd-architecture-20261029/architecture.json')
    assert architecture['input_md5'] == MD5
    names = {'ehsa_background_monitor', 'ehsa_common', 'ehsa_reg', 'ehsa_fsm', 'ehsa_ha',
             'platform_ehsa_registry', 'platform_ehsa', 'mcprp_ehsa_chain', 'mcprp_ha',
             'mcprp_peer_timeout', 'cmanrp', 'mcprp_red', 'ehsa_issu', 'rf_common', 'rf_master', 'rf_slave'}
    entities = [s for s in architecture['subsystems'] if s['name'] in names]
    got = load(folder/'runtime-got-bindings.json')
    assert got['input_md5'] == MD5 and got['base'] == base
    assert len(got['rows']) == 7
    profile = load(root/'profiles/ehsa_26_01_02.json')
    assert profile['input_md5'] == MD5
    for anchor in profile['function_anchors']:
        assert int(anchor['rva'], 0) in functions
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
              [folder/'fsm-tables.json', folder/'tables-and-imports.json', folder/'runtime-got-bindings.json',
               folder/'elf-boundaries-indexed.json', folder/'loaded-modules.json',
               root/'reports/iosd-architecture-20261029/architecture.json']}
    summary = {'schema_version': 1, 'input_md5': MD5, 'capture_base': base,
               'states': 14, 'event_cells': len(cells), 'distinct_action_callbacks': len(callbacks),
               'cells_with_callbacks': sum(r['callback_rva'] is not None for r in cells),
               'explicit_state_cells': sum(r['next_semantics'] == 'explicit_state' for r in cells),
               'saved_functions': len(functions), 'subsystem_records': len(entities),
               'source_sha256': hashes, 'function_evidence': list(functions.values()),
               'subsystems': entities, 'module_links': [r for r in architecture['module_links']
                    if 'ehsa' in (r.get('a', '') + r.get('b', '')).lower()],
               'runtime_got_bindings': got, 'unknowns': profile['unknowns'],
               'target_execution_changed': False, 'target_callbacks_executed': False,
               'runtime_fsm_state_read': False, 'all_state_reachability_proved': False,
               'table_verification': 'Complete saved bytes and consumer-derived layout; action semantics are reviewed decompilation, not execution tests'}
    (folder/'fsm-cells.json').write_text(json.dumps(cells, ensure_ascii=False, indent=2), encoding='utf-8')
    (folder/'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    doc = root/'docs/iosd的EHSA心跳与主备状态机.md'
    rendered = MarkdownIt('commonmark', {'html': False}).enable('table').render(doc.read_text(encoding='utf-8'))
    # Relative documentation links are rooted at docs; the evidence table below uses report-local links.
    rendered = re.sub(r'href="(?!https?:|#)([^\"]+)"', lambda m: 'href="' +
                      (m[1][len('../reports/ehsa-implementation-20261029/'):] if m[1].startswith('../reports/ehsa-implementation-20261029/') else '../../docs/'+m[1]) + '"', rendered)
    table = []
    for row in cells:
        cb = row['callback_rva']; proof = functions[cb]['source'] if cb is not None else None
        callback = '<a href="%s">0x%X</a>' % (escape(proof), cb) if proof else 'null（保留）'
        cols = [str(row['state'])+' '+(row['state_name'] or '未知名称'),
                '%s,%s → %s' % (row['major'], row['minor'], row['event_index']),
                row['event_name'] or '未知事件来源（保留）',
                '0x%X' % row['cell_rva'], callback,
                str(row['next_state_raw'])+' / '+row['next_semantics']]
        table.append('<tr>'+''.join('<td>'+ (v if i == 4 else escape(v))+'</td>' for i,v in enumerate(cols))+'</tr>')
    page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>iosd EHSA 心跳与主备状态机</title><style>body{font:16px/1.7 system-ui;margin:28px auto;padding:0 24px;max-width:1280px;color:#203041}pre{overflow:auto;background:#f0f4f8;padding:16px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:8px;border:1px solid #ced8e2;text-align:left;word-break:break-word}a{color:#075fa5}input{padding:10px;width:90%;margin:14px 0}h2{margin-top:36px}</style><body>__DOC__
<h2>完整状态事件表</h2><p>保留全部 224 个表项。可检索状态、事件、RVA、回调和未知项。表中 next=0 表示保持状态；表项存在不代表现场一定可达。原始字节和 JSON 可从 <a href="fsm-tables.json">捕获</a>、<a href="fsm-cells.json">解码表</a>、<a href="summary.json">证据摘要</a>核对。</p>
<input id="search" aria-label="检索状态事件表" placeholder="例如 WAIT_SWITCHOVER、未知、D51AF30"><p id="count"></p><table id="fsm"><thead><tr><th>当前状态</th><th>major,minor → 索引</th><th>事件来源</th><th>表项 RVA</th><th>动作回调</th><th>next 原始值 / 语义</th></tr></thead><tbody>__ROWS__</tbody></table>
<script>const rows=[...document.querySelectorAll('#fsm tbody tr')];function filter(){const q=document.querySelector('#search').value.toLowerCase();let n=0;for(const r of rows){r.hidden=!r.textContent.toLowerCase().includes(q);if(!r.hidden)n++;}document.querySelector('#count').textContent=n+' / '+rows.length+' 个表项';}document.querySelector('#search').addEventListener('input',filter);filter();</script></body></html>'''
    (folder/'index.html').write_text(page.replace('__DOC__', rendered).replace('__ROWS__', '\n'.join(table)), encoding='utf-8')
    return summary


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('analysis', type=Path)
    a = p.parse_args(); result = build(a.analysis.resolve(), Path(__file__).resolve().parents[1])
    print(json.dumps({k: result[k] for k in ('states', 'event_cells', 'distinct_action_callbacks', 'cells_with_callbacks', 'explicit_state_cells', 'saved_functions', 'subsystem_records')}))
