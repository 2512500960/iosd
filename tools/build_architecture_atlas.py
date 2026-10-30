"""Build eight evidence-scoped SVG diagrams and an offline iosd architecture reader."""
import argparse
from html import escape
import json
from pathlib import Path
import re
import unicodedata

from markdown_it import MarkdownIt

MD5='9eccfd46caadfff9c18557e2a446e19b'
FONT='Microsoft YaHei, Noto Sans CJK SC, sans-serif'


def wrapped(text,columns):
    lines=[];line='';width=0
    for char in text:
        step=2 if unicodedata.east_asian_width(char) in ('W','F') else 1
        if width+step>columns and line:lines.append(line);line='';width=0
        line+=char;width+=step
    if line:lines.append(line)
    return lines or ['']


class Diagram:
    def __init__(self,key,title,height=520,subtitle='关系示意；边上的文字说明连接方式，具体实现沿证据复核'):
        self.key=key;self.title=title;self.width=1120;self.height=height;self.nodes={};self.items=[]
        self.text(24,35,title,24,bold=True)
        self.text(24,64,subtitle,15,muted=True)

    def text(self,x,y,text,size=17,muted=False,bold=False,detail=False):
        cls='detail' if detail else ''
        self.items.append('<text class="%s" x="%s" y="%s" font-size="%s" fill="%s" font-weight="%s">%s</text>'%
                          (cls,x,y,size,'#526477' if muted else '#142c40',500 if bold else 400,escape(str(text))))

    def zone(self,x,y,w,h,label):
        self.items.append('<rect x="%s" y="%s" width="%s" height="%s" rx="14" fill="#f5f8fb" stroke="#ccd7df"/>'%(x,y,w,h))
        self.text(x+16,y+28,label,17,bold=True)

    def box(self,key,x,y,title,lines=(),w=240,h=86,tone='normal',detail=None):
        colors={'normal':('#e9f2fa','#9cb7cc'),'unknown':('#fff3df','#c9a971'),
                'state':('#e6f4ee','#91bba8'),'neutral':('#f0f3f6','#aab8c3')}
        fill,stroke=colors[tone];self.nodes[key]=(x,y,w,h)
        self.items.append('<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="%s" stroke="%s"%s/>'%
                          (x,y,w,h,fill,stroke,' stroke-dasharray="6 4"' if tone=='unknown' else ''))
        self.text(x+14,y+25,title,18,bold=True)
        textlines=[part for line in lines for part in wrapped(line,int((w-28)/7.7))]
        if 48+len(textlines)*21+(20 if detail else 0)>h+20:
            raise ValueError('Diagram text would overflow box: '+key)
        for index,line in enumerate(textlines):self.text(x+14,y+48+index*21,line,15)
        if detail:self.text(x+14,y+h-13,detail,13,muted=True,detail=True)

    def edge(self,a,b,label=None,dashed=False,side=None,via=()):
        ax,ay,aw,ah=self.nodes[a];bx,by,bw,bh=self.nodes[b]
        if side=='up':start=(ax+aw/2,ay);end=(bx+bw/2,by+bh)
        elif side=='down' or (by>ay+ah and side is None):start=(ax+aw/2,ay+ah);end=(bx+bw/2,by)
        elif side=='left':start=(ax,ay+ah/2);end=(bx+bw,by+bh/2)
        else:start=(ax+aw,ay+ah/2);end=(bx,by+bh/2)
        points=[start,*via,end]
        path='M '+' L '.join('%g %g'%p for p in points)
        self.items.append('<path d="%s" fill="none" stroke="#526e83" stroke-width="1.8" marker-end="url(#%s-arrow)"%s/>'%
                          (path,self.key,' stroke-dasharray="6 4"' if dashed else ''))
        if label:
            # Use explicit positions for elbow routes so labels stay outside nodes.
            text,x,y=label if isinstance(label,tuple) else (label,(start[0]+end[0])/2,(start[1]+end[1])/2-9)
            self.text(x,y,text,13,muted=True)

    def svg(self):
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 %s" role="img" aria-labelledby="%s-title %s-desc">'
                '<title id="%s-title">%s</title><desc id="%s-desc">样本 %s。实线为图中标明的局部关系，虚线含义按图例；未证明的边界保持未知。完整文字解释见对应文档。</desc>'
                '<defs><marker id="%s-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#526e83"/></marker></defs>'
                '<rect width="1120" height="%s" fill="#ffffff"/>'
                '<g font-family="%s">%s</g></svg>')%(self.height,self.key,self.key,self.key,escape(self.title),self.key,MD5,self.key,self.height,FONT,''.join(self.items))


def figures(layout):
    if layout['identity']['input_md5']!=MD5 or layout['section_overlaps']:
        raise ValueError('Atlas requires matching non-overlapping ELF layout')
    result={};mib=lambda n:n/1048576
    d=Diagram('elf','01 · 文件构成与加载后的内存',590,'原始 ELF 离线测量；MiB = 1,048,576 字节；按各类内容统计文件占用')
    d.text(24,108,'原始文件  %.2f MiB'%mib(layout['identity']['file_size']),20,bold=True)
    colors=['#426f98','#72a5bf','#8cbbad','#bdc7d2','#e4e9ee']
    labels=['可执行节','已分配只读数据','已分配可写数据','未分配元数据','头表、对齐等']
    keys=['executable','readonly_data','writable_data','nonallocated_metadata','headers_tables_padding_and_unassigned']
    start=24
    for index,(key,label) in enumerate(zip(keys,labels)):
        value=layout['file_buckets'][key];width=1072*value/layout['identity']['file_size']
        d.items.append('<rect x="%g" y="125" width="%g" height="40" fill="%s"/>'%(start,width,colors[index]));start+=width
        x=24 if index<3 else 590;y=203+index*30 if index<3 else 203+(index-3)*30
        d.items.append('<rect x="%s" y="%s" width="14" height="14" fill="%s"/>'%(x,y-12,colors[index]))
        d.text(x+24,y,'%s  %.2f MiB'%(label,mib(value)),16)
    d.zone(24,300,520,152,'可执行内容有不同区域和变体')
    d.text(40,359,'.text 311.40 MiB  /  CRPGC_text0 331.81 MiB',16)
    d.text(40,390,'BGP 有条件进入另一代码区的具体实例。',16)
    d.text(40,421,'其余函数的用途和对应关系沿具体入口分析。',15,muted=True)
    d.zone(570,300,526,152,'很小的元数据可以成为导航入口')
    d.text(586,359,'subsystem 区 0.52 MiB → 5,692 条记录',17)
    d.text(586,390,'module header 480 B / link 264 B',16)
    d.text(586,421,'8,866 个 .btrace* 名称节合计约 5.54 MiB',15,muted=True)
    d.text(24,501,'内存另算：NOBITS 按内存大小记录；PT_LOAD p_memsz 合计约 1,109.64 MiB。',17)
    d.text(24,535,'RSS 取决于页面驻留；进程还使用堆、线程栈和共享库，core 按已捕获页面读取。',15,muted=True)
    result['01-elf-layout']=d

    d=Diagram('views','02 · 四个视角一起解释 iosd',624)
    for x,w,label in [(24,520,'文件与进程边界'),(570,526,'初始化组织')]:d.zone(x,94,w,205,label)
    d.box('main',42,139,'iosd 主 ELF',['协议、CLI、公共设施与元数据'],w=236,h=100)
    d.box('so',306,139,'同进程共享库',['加载边界与实际绑定分别查'],w=220,h=100)
    d.edge('main','so',dashed=True)
    d.box('sub',588,139,'subsystem',['名字、类别、init、属性'],w=236,h=100)
    d.box('module',850,139,'module header / link',['分组、依赖、回调节点'],w=226,h=100)
    d.text(590,278,'两套机制在启动阶段协作，各有记录和消费路径。',15,muted=True)
    d.zone(24,326,520,215,'连接与执行设施')
    d.box('reg',42,373,'registry / 槽',['登记入口，分发者以后消费'],w=236,h=102)
    d.box('exec',306,373,'队列、task、pthread',['待处理对象与执行上下文'],w=220,h=102)
    d.edge('reg','exec',dashed=True)
    d.zone(570,326,526,215,'业务与状态')
    d.box('input',588,373,'CLI / 报文 / 事件',['各有入口、解析与条件'],w=236,h=102)
    d.box('state',850,373,'配置与运行状态',['对象、定时器、缓存、输出'],w=226,h=102,tone='state')
    d.edge('input','state')
    d.text(24,585,'虚线表示跨文件或登记连接；业务输入再沿消费路径进入状态处理。',15,muted=True)
    result['02-architecture-views']=d

    d=Diagram('init','03 · 启动编排分别推进两套初始化机制',690,'样本局部关系；地址为 RVA；类别与实际初始化顺序分别记录')
    d.box('entry',24,102,'ELF / libc 启动',['从入口进入 main 包装器'],w=242,h=104,detail='B2463A0 → B246530')
    d.box('proxy',304,102,'运行时代理',['接收应用回调'],w=242,h=104,detail='__be_pcohort_main_proxy')
    d.box('system',584,102,'应用回调与系统初始化',['成功分支准备运行环境'],w=242,h=104,detail='B2464A0 → D7B7690')
    d.edge('entry','proxy');d.edge('proxy','system',dashed=True,label=('回调边界',550,89))
    d.box('discover',584,258,'元数据发现与整理',['记录分别交给不同消费者'],w=242,h=104,detail='D710460 / D7127D0')
    d.edge('system','discover',side='down')
    d.box('subsys',154,423,'subsystem 机制',['类别、依赖、Pending → init'],w=360,h=110,detail='D710240 / D711090')
    d.box('modules',598,423,'module 机制',['分组 + 前置依赖 → 回调'],w=360,h=110,detail='D771FA0 / D771350 / D7715A0')
    d.edge('discover','subsys',side='down',via=[(705,393),(334,393)])
    d.edge('discover','modules',side='down',via=[(705,393),(778,393)])
    d.text(154,568,'5,692 条候选记录；13 类',18,bold=True)
    d.text(598,568,'15 个 header；11 条 link',18,bold=True)
    d.text(154,601,'类别用于安排初始化，init 执行具体准备工作。',15,muted=True)
    d.text(598,601,'已确认 memtest 归入 level_protocol 分组。',15,muted=True)
    d.text(24,653,'module 成员关系与 subsystem 分类各按本身的记录确定，并在启动路径中共同推进。',15,muted=True)
    result['03-initialization']=d

    d=Diagram('registration','04 · 初始化时登记，收到输入时消费',588,'关系示意；虚线表示函数指针的登记与读取，实际输入按对应接口分发')
    d.box('init',24,105,'功能 init',['准备状态与登记入口'])
    d.box('registry',304,105,'registry：key → callback',['保存实现的连接点'],w=300)
    d.edge('init','registry',label=('登记',270,135),dashed=True)
    d.box('packet',24,302,'输入到达',['报文、CLI、平台事件'])
    d.box('dispatch',304,302,'分发与条件检查',['选择键、模式或上下文'])
    d.box('callback',584,302,'被选中的 callback',['可以处理，也可以先入队'])
    d.edge('packet','dispatch');d.edge('dispatch','callback')
    d.edge('registry','dispatch',side='down',dashed=True,label=('读取已绑定入口',458,259))
    d.box('queue',584,464,'队列（部分机制有）',['保留待处理对象'])
    d.box('consumer',864,464,'消费者 / 状态更新',['task、事件循环或同步调用'],w=232,tone='state')
    d.edge('callback','queue',side='down',label=('可能入队',713,433));d.edge('queue','consumer')
    d.text(24,494,'需要两端证据：谁写入登记，谁查找并调用。',17)
    d.text(24,526,'名字与普通 xref 用于定位登记端和消费端的调查入口。',15,muted=True)
    result['04-registration-and-input']=d

    d=Diagram('cdp','05 · CDP 接收 队列与内部 task',660,'样本局部实现；虚线表示登记关系；队列将接收与后续解析连接起来')
    d.box('init',24,103,'CDP 初始化',['有条件地创建内部 task'],w=246,h=104,detail='CD878F0 / CD894C0')
    d.box('task',316,103,'CDP Protocol 入口',['创建队列并登记键 65'],w=246,h=104,detail='CD89F00')
    d.box('callback',24,305,'接收回调',['接口、启用、队列容量检查'],w=246,h=104,detail='CD8AB90')
    d.box('queue',316,305,'CDP packets 队列',['缓冲待处理报文'],w=246,h=104)
    d.box('loop',608,305,'task 事件循环取包',['取出报文后再检查上下文'],w=246,h=104,detail='CD89F00 / D789490')
    d.box('parser',608,493,'CDP 头 / TLV 检查',['版本、校验和、长度边界'],w=246,h=104,detail='CD8AF90')
    d.box('state',874,493,'邻居与计时状态',['缓存更新及扩展回调'],w=222,h=104,tone='state',detail='CD97B10 / CDAB1A0')
    d.edge('init','task');d.edge('task','callback',side='down',dashed=True,via=[(439,253),(147,253)],label=('登记键 65 与 callback',197,239))
    d.edge('callback','queue');d.edge('queue','loop');d.edge('loop','parser',side='down');d.edge('parser','state')
    d.text(24,488,'前面仍缺：平台入包到该回调的全部消费端。',16,muted=True)
    d.text(24,523,'后面仍缺：全部扩展 TLV / 后处理回调。',16,muted=True)
    d.text(24,625,'另一项 init 回调 CD9AE70 按接口清理邻居记录，与接收路径共同维护邻居状态。',16)
    result['05-cdp-path']=d

    d=Diagram('configuration','06 · CLI 修改状态，NVGEN 从状态生成文本',634,'关系示意与 hostname 案例；同一 handler 根据上下文分别执行输入和生成分支')
    d.box('cli',24,112,'CLI 文本输入',['关键字与参数'])
    d.box('parse',304,112,'parser / CSB',['匹配路径、设置上下文'])
    d.box('handler',584,112,'业务 handler 输入分支',['校验并修改配置状态'],h=108,detail='hostname: E0E6A00')
    d.box('state',864,112,'业务状态对象',['主机名、接口、协议配置'],w=232,h=108,tone='state')
    d.edge('cli','parse');d.edge('parse','handler');d.edge('handler','state')
    d.box('request',24,334,'显示或保存配置',['创建生成上下文'],h=108)
    d.box('engine',304,334,'NVGEN 调度',['语法、对象迭代与回调'],h=108,detail='E0DE210 / E39D8F0')
    d.box('generate',584,334,'业务 handler 生成分支',['读取相关状态并决定输出'],h=108,detail='hostname 同一 handler / selector')
    d.box('text',864,334,'配置文本输出',['公共输出封装 / 句柄'],w=232,h=108,detail='E0D9CD0 → E0D8B20')
    d.edge('request','engine');d.edge('engine','generate');d.edge('generate','text')
    d.edge('state','generate',side='down',via=[(980,278),(704,278)],label=('读取组件保存的配置状态',755,261))
    d.text(24,504,'接口缓存是有条件的生成优化：资格满足 + 命中 → 复用；否则生成并在相关路径保存。',17)
    d.text(24,547,'生成回调结合默认值和当前状态组织文本；命令定义、登记与门控保存在语法分析中。',17)
    d.text(24,590,'CSB 保存本次解析或生成的上下文，业务对象保存相应配置状态。',15,muted=True)
    result['06-cli-and-nvgen']=d

    d=Diagram('contexts','07 · Linux 线程 IOS task 与队列协作',650,'按已有创建与循环证据解释执行上下文、工作对象和业务回调')
    d.zone(24,102,1072,205,'同一个 iosd Linux 进程内：线程可跨主 ELF 和共享库执行代码')
    d.box('ios',42,151,'IOS 主线程',['已有线程被登记'],w=228,h=100)
    d.box('io',300,151,'Fastpath / Packet',['库中事件循环与 I/O 分发'],w=244,h=100)
    d.box('aux',574,151,'Auxiliary / Sim Aux',['请求队列、回调、通知'],w=244,h=100)
    d.box('workers',848,151,'Worker 线程池',['工作队列 → job 函数'],w=230,h=100)
    d.zone(24,355,516,205,'IOS 内部调度设施')
    d.box('tasks',42,404,'内部 task 的实例',['CDP Protocol / EHSA monitor','由 IOS 内部调度设施管理'],w=480,h=121)
    d.zone(570,355,526,205,'一个已核对的跨文件协作例子')
    d.box('soloop',588,404,'so 中 Auxiliary 循环',['等待请求、取得工作'],w=228,h=121)
    d.box('maincb',846,404,'主 ELF 接口与回调',['出队接口与业务代码','可在另一个文件中'],w=230,h=121)
    d.edge('soloop','maincb')
    d.text(24,607,'内部 task 到当前 Linux TID 的完整映射仍未知；需要现场栈、调度结构或消费记录。',17)
    result['07-execution-contexts']=d

    d=Diagram('ehsa','08 · EHSA：检测失联、推进状态、请求切换是不同阶段',650,'样本局部实现；虚线保留跨平台/外部消费端缺口；编号按所属消息或事件空间解释')
    d.box('receive',24,111,'KEEPALIVE 接收',['类型 30 → 登记回调'],w=246,h=108,detail='D51E0E0 → D512810')
    d.box('monitor',316,111,'刷新监测 / peer monitor',['定时或计数路径'],w=246,h=108,detail='D511EE0 / D510B80')
    d.box('filter',608,111,'失联事件过滤与策略',['raw event 与 FSM major/minor 分别记录'],w=274,h=108,detail='D50F450')
    d.edge('receive','monitor');d.edge('monitor','filter',label=('超时相关分支',571,96))
    d.box('fsm',608,325,'FSM 队列与内部 task',['当前状态 + major/minor → 动作'],w=274,h=108,detail='D519FC0 / D51A800')
    d.box('platform',316,325,'平台策略回调',['由平台 init 有条件安装'],w=246,h=108,detail='D52C3A0 / D52D8D0')
    d.box('external',24,325,'Chasfs / 外部消费者',['库绑定已有局部证据','外部接收与切换结果未闭合'],w=246,h=129,tone='unknown')
    d.edge('filter','fsm',side='down',label=('必要时投递事件',754,280))
    d.edge('filter','platform',side='down',via=[(745,270),(439,270)],label=('过滤器的策略 / 回调分支',452,254))
    d.edge('platform','external',side='left',dashed=True)
    d.text(24,518,'发送路径还经过传输槽与接口输出回调；部分具体运行时目标仍未恢复。',17)
    d.text(24,558,'发送、监测、事件投递、平台请求和切换完成，各有相应的处理与观测位置。',17)
    d.text(24,604,'平台实现与业务状态机通过回调和事件接口协作，外部消费端继续沿属性或消息查证。',15,muted=True)
    result['08-ehsa-boundaries']=d
    return result


def build(document,layout_path,assets,output):
    layout=json.loads(layout_path.read_text(encoding='utf-8'))
    drawings=figures(layout);assets.mkdir(parents=True,exist_ok=True)
    svgs={name:drawing.svg() for name,drawing in drawings.items()}
    for name,svg in svgs.items():(assets/(name+'.svg')).write_text(svg,encoding='utf-8',newline='\n')
    parser=MarkdownIt('commonmark',{'html':False}).enable('table')
    def image(tokens,index,options,environment):
        src=tokens[index].attrGet('src');name=Path(src).stem
        if name not in svgs:raise ValueError('Image not supplied by atlas builder: '+src)
        return '<figure tabindex="0">'+svgs[name]+'<figcaption>'+escape(tokens[index].content)+'</figcaption></figure>'
    parser.renderer.rules['image']=image
    tokens=parser.parse(document.read_text(encoding='utf-8'));entries=[]
    # A figure is a block, so do not wrap an image-only paragraph in <p>.
    for index,token in enumerate(tokens[:-2]):
        child=tokens[index+1]
        if token.type=='paragraph_open' and child.type=='inline' and child.children and len(child.children)==1 and child.children[0].type=='image':
            token.hidden=True;tokens[index+2].hidden=True
    topics=['file','structure','startup','structure','protocol','config','execution','ha','evidence']
    for index,token in enumerate(tokens):
        if token.type=='heading_open' and token.tag=='h2':
            anchor='atlas-%d'%(len(entries)+1);token.attrSet('id',anchor)
            entries.append({'id':anchor,'title':tokens[index+1].content,'topic':topics[len(entries)]})
    boundaries=[i for i,t in enumerate(tokens) if t.type=='heading_open' and t.tag=='h2']
    cover=parser.renderer.render(tokens[:boundaries[0]],parser.options,{})
    sections=[]
    for i,start in enumerate(boundaries):
        end=boundaries[i+1] if i+1<len(boundaries) else len(tokens)
        sections.append('<section data-topic="%s" id="section-%s">%s</section>'%
                        (entries[i]['topic'],entries[i]['id'],parser.renderer.render(tokens[start:end],parser.options,{})))
    nav=''.join('<a href="#%s" data-nav="%s">%s</a>'%(r['id'],r['id'],escape(r['title'])) for r in entries)
    html=PAGE.replace('__NAV__',nav).replace('__COVER__',cover).replace('__SECTIONS__',''.join(sections))
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(html,encoding='utf-8',newline='\n')
    return {'output':str(output),'diagrams':len(drawings),'sections':len(entries),
            'input_md5':layout['identity']['input_md5'],'source':'original ELF metadata and referenced prior evidence',
            'ida_access':False,'new_runtime_capture':False}


PAGE='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>看懂 iosd · 架构图解</title>
<style>
:root{font-family:"Microsoft YaHei",system-ui,sans-serif;color:#193045;background:#f5f7fa;font-size:17px;line-height:1.85}*{box-sizing:border-box}body{margin:0}header{padding:26px 34px;background:#142c40;color:#fff}header p{margin:4px 0 0;color:#d0dfeb;font-size:15px}header strong{font-size:25px;font-weight:500}a{color:#185c91;text-underline-offset:3px}nav{position:sticky;top:18px;align-self:start;max-height:95vh;overflow:auto;padding:18px;background:#fff;border-radius:12px}nav a{display:block;padding:7px 10px;text-decoration:none;color:#34536b;font-size:15px}nav a:hover{background:#e9f2fa}main{display:grid;grid-template-columns:235px minmax(0,1120px);gap:28px;max-width:1485px;margin:26px auto;padding:0 26px}article{min-width:0;background:#fff;padding:30px 34px;border-radius:12px}h1{font-size:29px;font-weight:500;line-height:1.5;margin:0 0 20px}h2{font-size:25px;font-weight:500;margin:0 0 22px;padding-top:18px;scroll-margin-top:20px}p{margin:15px 0}section{border-top:1px solid #dce5ec;padding:18px 0 24px}figure{margin:24px 0;overflow-x:auto;background:#fff;border:1px solid #e1e8ee;border-radius:10px}figure svg{display:block;width:100%;min-width:820px;height:auto}figcaption{font-size:14px;color:#526477;padding:9px 16px;border-top:1px solid #e1e8ee}table{display:block;overflow-x:auto;border-collapse:collapse;width:100%;font-size:15px}td,th{border:1px solid #d9e3eb;padding:10px 13px;text-align:left;min-width:110px}th{background:#f0f5f9;font-weight:500}code{font-family:Consolas,monospace;font-size:.88em;background:#eff4f8;padding:2px 4px;overflow-wrap:anywhere}.controls{display:flex;flex-wrap:wrap;gap:9px;align-items:center;padding:16px 0 22px}button,input{font:inherit;border:1px solid #b6c8d6;border-radius:7px;background:#fff;color:#193045;padding:7px 13px;font-size:15px}button{cursor:pointer}button[aria-pressed=true]{background:#193b55;color:#fff}input{flex:1;min-width:170px}label{font-size:14px}#count{font-size:14px;color:#526477;margin:0 0 18px}.hide-details .detail{visibility:hidden}[hidden]{display:none!important}.empty{padding:22px;background:#fff3df}footer{font-size:14px;color:#526477;padding-top:20px}.coverage{background:#edf5fb;padding:16px 20px;border-radius:9px;font-size:15px}
@media(max-width:1000px){main{display:block;padding:0 14px;margin:16px auto}nav{position:static;max-height:none;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:4px}nav a{font-size:14px}article{padding:22px 18px}header{padding:22px}h1{font-size:25px}h2{font-size:22px}}
@media print{header,nav,.controls,#count{display:none}main{display:block;margin:0;padding:0}article{padding:0}figure{break-inside:avoid}figure svg{min-width:0}section[hidden]{display:block!important}}
</style></head><body><header><strong>看懂 iosd</strong><p>先看关系，再看函数 · 文件 / 初始化 / 执行上下文 / 输入与状态</p></header><main><nav aria-label="文档目录">__NAV__</nav><article>
<div class="coverage">适用样本：C8000v 26.01.02。八张图结合原始 ELF 测量、初始化记录和已核对的局部实现，具体覆盖范围见证据小节。</div>
<div class="controls"><input id="search" type="search" aria-label="搜索图解内容" placeholder="搜索：队列、NVGEN、subsystem…"><button data-filter="all" aria-pressed="true">完整阅读</button><button data-filter="file" aria-pressed="false">文件大小</button><button data-filter="protocol" aria-pressed="false">协议流程</button><button data-filter="config" aria-pressed="false">配置生成</button><label><input id="details" type="checkbox" checked>显示图中地址细节</label><button id="reset">重置</button></div>
<p id="count" role="status"></p><div id="cover">__COVER__</div><div id="chapters">__SECTIONS__</div><p id="empty" class="empty" hidden>没有匹配的内容。可清空搜索或选择完整阅读。</p>
<footer>本页离线工作，不连接 IDA、设备或外部网络。图解用于定位和理解；具体实现按样本、条件和证据复核。</footer></article></main>
<script>
(()=>{const sections=[...document.querySelectorAll('section[data-topic]')],buttons=[...document.querySelectorAll('button[data-filter]')],nav=[...document.querySelectorAll('nav a')];let topic='all';const search=document.getElementById('search'),details=document.getElementById('details');
function update(){let count=0;const query=search.value.trim().toLowerCase();sections.forEach((s,i)=>{s.hidden=!(topic==='all'||s.dataset.topic===topic)||!s.textContent.toLowerCase().includes(query);nav[i].hidden=s.hidden;if(!s.hidden)count++});document.getElementById('count').textContent='显示 '+count+' / '+sections.length+' 个部分。窄屏可横向滚动查看图。';document.getElementById('empty').hidden=count!==0;buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===topic)));document.getElementById('cover').hidden=topic!=='all'||Boolean(query)}
buttons.forEach(b=>b.addEventListener('click',()=>{topic=b.dataset.filter;update()}));search.addEventListener('input',update);details.addEventListener('change',()=>document.body.classList.toggle('hide-details',!details.checked));document.getElementById('reset').addEventListener('click',()=>{search.value='';topic='all';details.checked=true;document.body.classList.remove('hide-details');update()});update()})();
</script></body></html>'''


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--document',required=True,type=Path);p.add_argument('--layout',required=True,type=Path)
    p.add_argument('--assets',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    a=p.parse_args();print(json.dumps(build(a.document,a.layout,a.assets,a.output),ensure_ascii=False))


if __name__=='__main__':main()
