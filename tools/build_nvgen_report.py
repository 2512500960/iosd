"""Build a local NVGEN evidence catalogue; no IDA or target connection."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.catalogue import inventory_html


def main():
    cli=argparse.ArgumentParser(description=__doc__);cli.add_argument('analysis');cli.add_argument('--profile',default='profiles/nvgen_26_01_02.json')
    args=cli.parse_args();root=Path(args.analysis)
    summary=json.loads((root/'binding-summary.json').read_text(encoding='utf-8'))
    profile=json.loads(Path(args.profile).read_text(encoding='utf-8'))
    if summary['identity']['input_md5']!=profile['input_md5']:raise ValueError('Profile/capture mismatch')
    base=summary['identity']['imagebase'];callbacks=[]
    for line in (root/'cli-nvgen-associations.jsonl').open(encoding='utf-8'):
        row=json.loads(line)
        callbacks.append({'node_rva':hex(row['node']-base) if base<=row['node']<base+0x50000000 else None,
                          'callback_rva':hex(row['callback_rva']) if row['callback_rva'] is not None else None,
                          'callback_capture_va':hex(row['callback']) if row['callback'] else None,
                          'selector':row['selector'],'flags':row['flags_raw_hex'],
                          'same_function_eol_nodes':len(row['cli_terminal_matches']),
                          'same_function_selector_eol_nodes':len(row['same_function_and_selector_matches']),
                          'dispatch_verified':row['dispatch_verified']})
    steps=[('显示配置','0xDFE9DB0 → 0xDFE8DD0','生成请求经 E0D71A0/回退 E0D6360 进入公共设施'),
           ('生成上下文','0xE0D6470 → 0xE0DE210','NV Parser CSB；NVGEN=1；模式、输出目标及钩子'),
           ('遍历配置语法','0xDF3CA50 → 0xDEE5040 → 0xDEE5E30','普通分支取得 mode+0x50 根并调度动作；指定回调另有分支'),
           ('调用生成回调','0xE39D8F0 → 0xE39D9B0','读取 selector/flags，按状态门控调用'),
           ('输出文本','0xE0D9CD0 → 0xE0D8B20 → 0xE0E1B20','格式化、缩进、写入输出设施'),
           ('缓存开关','0xDEF9650；变量 0x381C05B0','存在命令实现，当前目标启用值未读取'),
           ('缓存命中','0xDEF99C0 → 0xDEF9790 → 0xDEF9A20','除开关外还受接口类型、输出上下文及回调条件控制'),
           ('保存缓存','0xE3FC1B0 → 0xE0D5E90','截取生成片段到接口对象+544'),
           ('禁用清理','0xDF331E0 → 专用语法链 → 0xDF34330','接口迭代后释放缓存；不是重跑 subsystem init')]
    data={'identity':summary['identity'],'summary':{k:v for k,v in summary.items() if k!='identity'},
          'coverage':{'scope':profile['scope'],'all_update_invalidation_triggers_recovered':False},
          'labels':{'flow':'生成与缓存流程','examples':'已核对的共用 handler 案例','callbacks':'NVGEN 描述符与 EOL 关联','unknown':'保留的缺口'},
          'tables':{'flow':[{'stage':s,'rva_chain':r,'meaning':m} for s,r,m in steps],
                    'examples':profile['examples'],'callbacks':callbacks,
                    'unknown':[{'gap':x} for x in profile['unresolved']]}}
    html=inventory_html(data,'iosd NVGEN 与接口配置缓存',
        'NVGEN 沿配置语法、对象迭代和生成钩子调用回调，由业务代码读取状态并输出文本。这里展示保存的定义和已核对的实现；不调用目标函数，不把节点数当作命令数。',
        '完整解释见 docs/iosd的NVGEN与接口配置缓存.md。原始条件和未知分支仍在保存图中；本页关联不证明当前可达或缓存已启用。')
    (root/'index.html').write_text(html,encoding='utf-8')
    print(json.dumps({'callbacks':len(callbacks),'output':str((root/'index.html').resolve())},ensure_ascii=False))


if __name__=='__main__':main()
