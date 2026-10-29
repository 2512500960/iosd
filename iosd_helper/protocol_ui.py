"""Native chooser navigation from protocol clues to bounded IDA relationships."""
import ida_kernwin as kw
import ida_segment

from .ida_adapter import identity
from .protocol_ida import collect_protocol, relationships


class ProtocolBrowser:
    def __init__(self, app):self.app = app

    def find(self):
        query = kw.ask_str('cdp', 0, 'Protocol identifier: cdp / bgp / ospf / isis / ...')
        if query is None:return
        kw.show_wait_box('Collecting protocol clues from saved IDB only\nCancel keeps partial results.')
        try:
            result = collect_protocol(query, getattr(self.app, 'architecture_model', None), kw.user_cancelled)
        finally:kw.hide_wait_box()
        result['relationships'] = []
        self.app.last = result
        kw.msg('[iosd-helper] %s: %d subsystem metadata candidates, %d name/literal clues. '
               'Packet processing path is not yet verified. Export last result saves the plan and visited relationships.\n' %
               (query, len(result['subsystems']), len(result['candidates'])))
        self.browse(result)

    def check(self, result):
        current = identity()
        if current['input_md5'].lower() != result['identity']['input_md5'].lower():
            raise ValueError('Protocol evidence belongs to a different binary')
        return current

    def resolve(self, result, row):
        current = self.check(result)
        if row.get('rva') is not None:ea = current['imagebase']+row['rva']
        else:
            if current['imagebase'] != result['identity']['imagebase']:
                raise ValueError('Unclassified/external address cannot be reused after rebase; rescan')
            ea = row.get('ea')
        if ea is None or ida_segment.getseg(ea) is None:raise ValueError('Address not mapped in the current IDB')
        return ea

    def browse(self, result):
        options = [('Investigation plan / 如何追踪报文', lambda:self.app.evidence(result['plan'])),
                   ('Subsystem init candidates / 子系统初始化线索', lambda:self.candidates(result, result['subsystems'])),
                   ('Names, strings and source clues / 名称、字符串与源码线索', lambda:self.candidates(result, result['candidates'])),
                   ('Coverage and unknowns / 扫描范围与缺口', lambda:self.app.evidence({
                       'coverage':result['coverage'], 'faults':result['faults'], 'limits':result['plan']['limits']}))]
        self.app.table('Protocol %s: investigation entry points' % result['protocol'], [('View',100)],
                       [[label] for label,_ in options], lambda n:self.app.guard(options[n][1]))

    def candidates(self, result, rows):
        self.check(result)
        def detail(n):
            row = rows[n]
            actions = [('Evidence + jump / 查看证据并跳转', lambda:self.app.evidence(row,self.resolve(result,row))),
                       ('Explore one hop / 调用、引用与未知回调', lambda:self.explore(result,row))]
            self.app.table('Protocol clue', [('Action',100)], [[label] for label,_ in actions],
                           lambda i:self.app.guard(actions[i][1]))
        self.app.table('%s: candidates, not packet handler assignments' % result['protocol'],
            [('Kind',26),('Name / literal',100),('RVA / captured EA',24),('Category / location',32),('Evidence',70)],
            [[r['kind'],r['name'][:600],hex(r['rva']) if r.get('rva') is not None else hex(r['ea']) if 'ea' in r else '?',
              r.get('category',r.get('location','unknown')),r['evidence']] for r in rows],
            lambda n:self.app.guard(lambda:detail(n)))

    def explore(self, result, row, address_context=None):
        ea = self.resolve(address_context or result, row)
        if len(result['relationships']) >= 100:
            raise ValueError('100 visited relationship captures retained; export and start a new protocol investigation')
        kw.show_wait_box('Inspecting one function / incoming references\nCancel keeps partial evidence.')
        try:graph = relationships(ea,kw.user_cancelled)
        finally:kw.hide_wait_box()
        result['relationships'].append(graph);self.app.last = result
        kw.msg('[iosd-helper] Protocol relationship coverage: %s\n' % graph['coverage'])
        def detail(n):
            edge = graph['rows'][n]
            actions = [('Evidence + source jump', lambda:self.app.evidence(edge,self.resolve(graph,edge['site'])))]
            if edge.get('target'):
                actions.append(('Inspect target one hop (does not assert packet flow)',lambda:self.explore(result,edge['target'],graph)))
            self.app.table('Relationship evidence', [('Action',105)], [[label] for label,_ in actions],
                           lambda i:self.app.guard(actions[i][1]))
        self.app.table('%s: one-hop relationships (includes unresolved calls)' % result['protocol'],
            [('Relation',38),('Site RVA / EA',23),('Target RVA / EA',23),('Target name',70)],
            [[r['kind'],hex(r['site']['rva']) if r['site']['rva'] is not None else hex(r['site']['ea']),
              hex(r['target']['rva']) if r.get('target') and r['target']['rva'] is not None else
              hex(r['target']['ea']) if r.get('target') else '?',r.get('name','')] for r in graph['rows']],
            lambda n:self.app.guard(lambda:detail(n)))
