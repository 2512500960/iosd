"""Protocol investigation plans and evidence candidates, independent of IDA."""
import re


def protocol_query(query):
    query = query.strip().lower()
    if not re.fullmatch(r'[a-z][a-z0-9_-]{1,39}', query):
        raise ValueError('Use a protocol identifier such as cdp, bgp, ospf or isis (2–40 characters)')
    return query


def match_kind(text, query):
    query = protocol_query(query)
    if query not in text.lower():return None
    return 'name_token_candidate' if re.search(r'(?<![a-z0-9])'+re.escape(query)+r'(?![a-z0-9])', text.lower()) else 'substring_candidate'


def subsystem_seeds(model, identity, query):
    if model.get('input_md5', '').lower() != identity['input_md5'].lower():
        raise ValueError('Subsystem index belongs to a different binary')
    if model.get('address_space') != 'rva':raise ValueError('Subsystem index must use RVAs')
    rows = []
    for row in model['subsystems']:
        kind = match_kind(row['name'], query)
        if kind:
            rows.append({'kind': 'subsystem_metadata', 'name': row['name'], 'match': kind,
                         'rva': row['init_rva'], 'record_rva': row['record_rva'],
                         'category': row['category'], 'evidence': 'saved subsystem header/init candidate; execution and packet role unverified'})
    return sorted(rows, key=lambda row: (row['name'].lower() != query, row['match'] != 'name_token_candidate', row['name']))


def investigation_plan(query):
    query = protocol_query(query)
    common = [
        {'stage': '初始化与注册', 'question': '哪个 subsystem init 安装了收包、TCP 或 registry 回调？',
         'look_for': '从 metadata init 出发检查直接调用和作为参数传递的代码地址；回调指针引用仅是候选，需核对注册 API、槽位及条件。'},
        {'stage': '接收与分发', 'question': '数据从哪个接收入口、队列或 socket 到达协议函数？',
         'look_for': '沿回调消费端反向核对注册者；记录缓冲区来源、长度、接口/邻居上下文。分清 IOS task 和 Linux pthread。'},
        {'stage': '报文解析', 'question': '谁检查报文头、长度和类型，谁处理各字段？',
         'look_for': '检查字段读取、字节序、分支/分发表、长度约束和错误处理；保留尚未解析的间接调用。'},
        {'stage': '状态与结果', 'question': '解析后改变了哪些邻居、路由或协议状态？',
         'look_for': '跟踪解析结果到状态对象、定时器和事件队列；CLI handler 往往配置状态，不能直接等同网络报文入口。'},
        {'stage': '代码归属', 'question': '实现位于主 ELF、外部 so，还是经 IPC 交给其他进程？',
         'look_for': '区分 .text、extern、PLT/GOT、运行时绑定和 IPC 接收方；一个导入名称或 IPC 字符串不能证明外部实现及 PID。'},
    ]
    specific = {
        'cdp': {'focus': '按二层接收/分发 → CDP 头与 TLV 检查 → 邻居状态的方向调查；这只是协议分析路线，不是当前样本已证明的调用链。',
                'terms': ['CDP Protocol', 'cdp_input', 'cdp_receive', 'cdp_process', 'TLV', 'checksum', 'holdtime'],
                'source': 'https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/cdp/configuration/xe-17/cdp-xe-17-book.html'},
        'bgp': {'focus': '先找 TCP 会话的读取与消息组装，再看报文头及 OPEN / UPDATE / KEEPALIVE / NOTIFICATION 分发；路由策略与 RIB 更新属于后续阶段。',
                'terms': ['BGP Router', 'BGP I/O', 'bgp_read', 'bgp_input', 'OPEN', 'UPDATE', 'NOTIFICATION', 'KEEPALIVE'],
                'source': 'https://www.rfc-editor.org/rfc/rfc4271'},
    }
    return {'protocol': query, 'stages': common, 'protocol_hint': specific.get(query, {
        'focus': '从初始化、输入注册、解析分发和状态更新四个方向交叉定位。', 'terms': [query], 'source': None}),
        'limits': ['名称、日志和源码路径是搜索线索；不会自动证明报文处理角色或组件包含关系。',
                   '直接调用关系不等于网络数据流；静态路径也不证明当前配置下可达。',
                   '没有引用不等于没有实现：大端/tagged 指针、动态注册和未分析代码可能没有普通 IDA xref。',
                   '一次扫描受名称数、字节数、结果数限制，未扫描和未解析的部分必须继续保留。']}
