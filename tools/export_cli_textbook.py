"""Export hash-verified CLI witnesses as small, linked GitHub-readable Markdown files."""
import argparse
from collections import Counter
import gzip,hashlib,html,json,re,sqlite3,tempfile
from pathlib import Path


MODELS={
    'baseline':('六个基础模式的历史连接','cli/catalogue.jsonl.gz'),
    'observed':('补充模式入口与历史连接','unbound-cli/observed_connections.jsonl.gz'),
    'conditional':('已捕获槽位上的条件安装','unbound-cli/conditional_registration_candidates.jsonl.gz'),
    'slot-creation':('依赖静态建槽的条件安装','unbound-cli/static_slot_creation_candidates.jsonl.gz'),
    'other':('其他模式的历史连接','unbound-cli/other_mode_connections.jsonl.gz')}
FIELDS={'conditions':('C','条件'),'parameters':('P','参数'),'gaps':('G','缺口'),
        'state_effects':('S','状态效果'),'conditional_registrations':('R','候选注册')}
CATEGORIES={'registration_fragment_without_acquired_mode_path':'注册片段已有，模式路径待补',
    'pending_fragment_without_mode_path':'历史 pending 片段，模式路径待补',
    'bound_fragment_without_acquired_mode_path':'观察到绑定，模式路径待补',
    'no_acquired_mode_or_registration_path':'模式与注册路径待补'}


def packed(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def digest(value):return hashlib.sha256(value).hexdigest()
def rows(path):
    with gzip.open(path,'rt',encoding='utf-8') as stream:
        for line in stream:
            if line.strip():yield json.loads(line)


def slug(mode):
    stem=re.sub('[^a-zA-Z0-9_-]+','-',mode).strip('-')[:52] or 'unknown'
    return 'm-'+stem+'-'+digest(mode.encode())[:8]


def label(value):return html.escape(str(value),quote=False).replace('|','\\|').replace('[','\\[').replace(']','\\]').replace('\n',' ')
def inline(value):
    text=str(value).replace('\n',' ');fence='`'*(max([len(x) for x in re.findall('`+',text)]+[0])+1)
    return fence+' '+text+' '+fence


def fenced(value,language='text'):
    fence='`'*max(3,max([len(x) for x in re.findall('`+',value)]+[0])+1)
    return fence+language+'\n'+value+'\n'+fence+'\n'


def address(ref):
    if not ref:return '未知'
    if 'node_rva' in ref:return 'RVA 0x%X'%ref['node_rva']
    if 'node_captured_va' in ref:return '历史 VA 0x%X'%ref['node_captured_va']
    if ref.get('space')=='image':return 'RVA 0x%X'%ref['rva']
    if ref.get('space')=='captured_runtime':return '历史 VA 0x%X'%ref['va']
    return packed(ref)


def pretty_addresses(value):
    if isinstance(value,list):return [pretty_addresses(x) for x in value]
    if not isinstance(value,dict):return value
    return {k:('0x%X'%v if isinstance(v,int) and (k.endswith('_rva') or k.endswith('_captured_va')) else pretty_addresses(v)) for k,v in value.items()}


def paginate(items,prefix,max_bytes,max_entries=400):
    """Keep whole entries together and reject any single entry larger than the page budget."""
    page=[];size=len(prefix.encode());number=1
    for identifier,block in items:
        length=len(block.encode())
        if length+len(prefix.encode())>max_bytes:raise ValueError('Single entry exceeds page budget: '+identifier)
        if page and (size+length>max_bytes or len(page)>=max_entries):
            yield number,prefix+''.join(x[1] for x in page),[x[0] for x in page]
            page=[];size=len(prefix.encode());number+=1
        page.append((identifier,block));size+=length
    if page:yield number,prefix+''.join(x[1] for x in page),[x[0] for x in page]


class Registry:
    def __init__(self,db):
        self.db=db
        db.execute('CREATE TABLE atoms(id TEXT PRIMARY KEY,field TEXT,payload TEXT)')
        db.execute('CREATE TABLE chains(id TEXT PRIMARY KEY,field TEXT,payload TEXT)')

    def save(self,table,field,value):
        payload=packed(value);prefix=FIELDS[field][0]+('a' if table=='atoms' else '')
        identifier=prefix+'-'+digest(payload.encode())[:16]
        old=self.db.execute('SELECT payload FROM '+table+' WHERE id=?',(identifier,)).fetchone()
        if old and old[0]!=payload:raise ValueError('Evidence identifier collision')
        if not old:self.db.execute('INSERT INTO '+table+' VALUES(?,?,?)',(identifier,field,payload))
        return identifier

    def chain(self,field,values):
        if not values:return None
        return self.save('chains',field,[self.save('atoms',field,v) for v in values])


def verify_sources(version):
    baseline=json.loads((version/'cli/summary.json').read_text(encoding='utf-8'))
    followup=json.loads((version/'unbound-cli/manifest.json').read_text(encoding='utf-8'))
    if baseline['identity']['input_md5']!=followup['identity']['input_md5']:raise ValueError('Mixed sample identities')
    files={path for _,path in MODELS.values()}|{'unbound-cli/terminals.jsonl.gz'}
    hashes={}
    for relative in sorted(files):
        path=version/relative;sha=digest(path.read_bytes())
        expected=baseline['artifact_sha256'].get(path.name) if relative.startswith('cli/') else followup['artifact_sha256'].get(relative)
        if sha!=expected:raise ValueError('Source hash differs: '+relative)
        hashes[relative]=sha
    return baseline['identity'],hashes


def build_book(version,output,max_bytes=196608):
    version=version.resolve();output=output.resolve()
    # A book is generated beneath its version directory; other trees are never cleanup targets.
    output.relative_to(version)
    if output==version:raise ValueError('Use a dedicated output subdirectory')
    identity,hashes=verify_sources(version)
    output.mkdir(parents=True,exist_ok=True);written={};previous=output/'manifest.json'
    old=json.loads(previous.read_text(encoding='utf-8')).get('artifact_sha256',{}) if previous.exists() else {}
    def write(relative,text):
        path=output/relative;path.resolve().relative_to(output)
        path.parent.mkdir(parents=True,exist_ok=True);data=(text.rstrip()+'\n').encode('utf-8')
        if len(data)>max_bytes:raise ValueError('Generated page too large: '+relative)
        path.write_bytes(data);written[relative]=digest(data)
    with tempfile.TemporaryDirectory(prefix='iosd-cli-text-') as temporary:
        db=sqlite3.connect(str(Path(temporary)/'book.sqlite'))
        try:
            db.execute('CREATE TABLE paths(model TEXT,mode TEXT,syntax TEXT,prompt TEXT,root INTEGER,evidence TEXT,payload TEXT,PRIMARY KEY(model,evidence))')
            registry=Registry(db);counts=Counter();mode_counts=Counter();unique_eols=set()
            for model,(_,relative) in MODELS.items():
                for row in rows(version/relative):
                    counts[model]+=1;mode_counts[row['mode']]+=1;unique_eols.add(packed(row['eol_node']))
                    compact={k:row.get(k) for k in ('handler','eol_node','selector_candidate','syntax_status','final_tracked_state','mode_candidates','mode_aliases')}
                    compact['references']={f:registry.chain(f,row.get(f,[])) for f in FIELDS}
                    compact['parameter_help']=[{'kind':p.get('kind'),'help':p.get('help')} for p in row.get('parameters',[]) if p.get('help')]
                    db.execute('INSERT INTO paths VALUES(?,?,?,?,?,?,?)',(model,row['mode'],row['syntax_candidate'],row['prompt'],row.get('mode_root_rva',-1),row['evidence_id'],packed(compact)))
                print(packed({'stage':'imported','model':model,'records':counts[model]}),flush=True)
            db.commit();db.execute('CREATE INDEX mode_order ON paths(mode,model,syntax,prompt,root,evidence)')
            links={};reference_pages=[]
            for table in ('atoms','chains'):
                for field,(_,title) in FIELDS.items():
                    def entries():
                        for identifier,payload in db.execute('SELECT id,payload FROM '+table+' WHERE field=? ORDER BY id',(field,)):
                            value=json.loads(payload)
                            block='### '+identifier+'\n\n'
                            if table=='atoms':block+=fenced(json.dumps(pretty_addresses(value),ensure_ascii=False,indent=2),'json')+'\n'
                            else:block+=' → '.join('['+i+']('+links[i]+'#'+i.lower()+')' for i in value)+'\n\n'
                            yield identifier,block
                    name=field+('-items' if table=='atoms' else '-sets')
                    prefix='# '+title+('明细' if table=='atoms' else '序列')+'\n\n[返回参考索引](README.md) · [阅读说明](../README.md)\n\n'
                    for number,text,ids in paginate(entries(),prefix,max_bytes):
                        filename=name+'-%03d.md'%number
                        write('evidence/'+filename,text);reference_pages.append((title,table,filename,len(ids)))
                        for identifier in ids:links[identifier]=filename
            reference_index=['# 条件、参数、状态和缺口参考\n\n','[命令总索引](../README.md)\n\n',
                '命令页链接到“序列”，按路径顺序列出明细 ID。明细保留已取得字段；映像地址显示为十六进制 RVA，历史运行时地址标为 captured VA。\n\n',
                '`kind` 表示动作种类；`function_rva` 是回调；`expected` 是路径所需结果；`evaluated=false` 表示符号约束；`evaluated=true` 按该动作的静态模型解释。`field_offset` 是结构偏移，`min/max` 是参数范围。\n\n',
                '状态效果是路径中的赋值或回调模型，设备上的实际效果另按执行证据判断。缺口字段包括未知动作、描述符、回调和条件安装。候选注册保留 key、类型、创建点和安装状态。\n\n',
                '| 内容 | 分页 | 条目 |\n|---|---|---:|\n']
            for title,table,filename,count in reference_pages:
                reference_index.append('| '+title+('明细' if table=='atoms' else '序列')+' | ['+filename+']('+filename+') | '+str(count)+' |\n')
            write('evidence/README.md',''.join(reference_index))
            mode_index=[];exported=0;command_pages=0
            for (mode,) in db.execute('SELECT DISTINCT mode FROM paths ORDER BY mode'):
                directory='modes/'+slug(mode);mode_lines=['# 模式 '+label(mode)+'\n\n','[命令总索引](../../README.md) · [参考说明](../../evidence/README.md)\n\n',
                    '每条记录对应一个已取得的 EOL/跟踪上下文路径。相同语法的不同 selector、条件和状态分别保存。模式根、同根候选名称和父模式在页首列出；进入该模式的命令需另沿 handler 关联。\n\n']
                root_rows=db.execute('SELECT DISTINCT root,payload FROM paths WHERE mode=?',(mode,))
                definitions={};aliases=set()
                for root,payload in root_rows:
                    row=json.loads(payload);aliases.update(row.get('mode_aliases') or [])
                    for item in row.get('mode_candidates') or []:definitions[(root,packed(item))]=item
                if aliases:mode_lines.append('同根名称候选：'+', '.join(inline(x) for x in sorted(aliases))+'。\n\n')
                for (root,_),item in sorted(definitions.items()):
                    mode_lines.append('- 根 '+inline('RVA 0x%X'%root)+'；名称 '+inline(item.get('name'))+'；提示符 '+inline(item.get('prompt'))+'；parent '+inline(item.get('parent'))+'；'+inline(item['id'])+'。\n')
                mode_lines.append('\n| 证据模型 | 命令文本 | 参数与证据 | 首条 → 末条 | 路径记录 |\n|---|---|---|---|---:|\n')
                for model,(description,_) in MODELS.items():
                    query=db.execute("SELECT syntax,prompt,root,evidence,payload FROM paths WHERE mode=? AND model=? ORDER BY (substr(syntax,1,1)='<'),syntax,prompt,root,evidence",(mode,model))
                    entry_info={}
                    def entries():
                        for syntax,prompt,root,evidence,payload in query:
                            entry_info[evidence]=(prompt,syntax)
                            row=json.loads(payload)
                            block='### '+evidence+'\n\n'+fenced('('+prompt+')# '+syntax)+'\n'
                            block+='Handler '+inline(address(row['handler']))+'；selector '+inline(row['selector_candidate'])+'；EOL '+inline(address(row['eol_node']))+'。\n\n'
                            if root>=0:block+='模式根 '+inline('RVA 0x%X'%root)+'；'
                            block+='语法状态 '+inline(row['syntax_status'])+'；跟踪状态 '+inline(packed(row['final_tracked_state']))+'。\n\n'
                            if row['parameter_help']:
                                block+='参数提示：'+'；'.join(inline(p['kind'])+' '+label(p['help']) for p in row['parameter_help'])+'。\n\n'
                            refs=['['+FIELDS[f][1]+' '+i+'](../../evidence/'+links[i]+'#'+i.lower()+')' for f,i in row['references'].items() if i]
                            block+=(' · '.join(refs) if refs else '该路径记录的参数、条件、状态效果和缺口列表均为空。')+'\n\n'
                            yield evidence,block
                    prefix='# '+label(mode)+' · '+description+'\n\n[模式索引](README.md) · [总索引](../../README.md)\n\n'
                    for number,text,ids in paginate(entries(),prefix,max_bytes):
                        filename=model+'-%03d.md'%number;write(directory+'/'+filename,text)
                        plain=model+'-%03d.txt'%number
                        lines=['# 模式 '+mode+'；'+description+'\n','# 每行一条路径见证；末尾编号对应同名 Markdown 页。\n',
                            '# 详细参数、handler、条件和缺口：'+filename+'\n\n']
                        for evidence in ids:
                            prompt,syntax=entry_info[evidence]
                            lines.append('('+prompt+')# '+syntax+'    # '+evidence+'\n')
                        write(directory+'/'+plain,''.join(lines))
                        interval=inline(entry_info[ids[0]][1])+' → '+inline(entry_info[ids[-1]][1])
                        mode_lines.append('| '+description+' | ['+plain+']('+plain+') | ['+filename+']('+filename+') | '+interval+' | '+str(len(ids))+' |\n')
                        exported+=len(ids);command_pages+=1
                write(directory+'/README.md',''.join(mode_lines));mode_index.append((mode,directory,mode_counts[mode]))
            unresolved=Counter();unresolved_pages=[]
            def unresolved_entries():
                for row in rows(version/'unbound-cli/terminals.jsonl.gz'):
                    if row['category'] in {'additional_config_mode_root','config_candidate_registration_edge','config_static_slot_creation_candidate','additional_other_mode_root'}:continue
                    unresolved[row['category']]+=1;identifier='terminal-'+digest(packed(row['eol']).encode())[:16]
                    block='### '+identifier+'\n\n'+CATEGORIES.get(row['category'],row['category'])+'。\n\n'
                    block+='终点 '+inline(address(row['eol']))+'；handler '+inline(address(row.get('handler')))+'；selector '+inline(row.get('selector_candidate'))+'。\n\n'
                    detail={k:row[k] for k in ('registration_root_associations','remaining_uncertainties','observed_mode_candidates','registration_overlay_mode_candidates','static_slot_creation_mode_candidates') if row.get(k)}
                    if detail:block+=fenced(json.dumps(pretty_addresses(detail),ensure_ascii=False,indent=2),'json')+'\n'
                    yield identifier,block
            prefix='# 尚缺模式路径的终止定义\n\n[总索引](../README.md)\n\n这些记录保留终点及已有局部线索，完整命令语法仍待恢复。\n\n'
            for number,text,ids in paginate(unresolved_entries(),prefix,max_bytes):
                name='unresolved/part-%03d.md'%number;write(name,text);unresolved_pages.append((name,len(ids)))
            index=['# 尚缺模式路径的候选\n\n[命令总索引](../README.md)\n\n']
            for category,count in unresolved.items():index.append('- '+CATEGORIES.get(category,category)+'：'+str(count)+'。\n')
            index.append('\n')
            for name,count in unresolved_pages:index.append('- ['+name.split('/')[-1]+']('+name.split('/')[-1]+')：'+str(count)+' 项。\n')
            write('unresolved/README.md',''.join(index))
            assert exported==sum(counts.values()),'Lost witness records'
            intro=['# iosd 命令文本目录\n\n',
                'C8000v IOS XE 26.01.02，样本 MD5 '+inline(identity['input_md5'])+'。本目录将已恢复路径整理成小型 Markdown 文本，点击模式即可在 GitHub 阅读。\n\n',
                '**路径记录 '+format(exported,',')+' 条，涉及 '+str(len(mode_index))+' 个主名称；跨模式合计 '+format(len(unique_eols),',')+' 个不同 EOL。**相同命令文本可以对应多个上下文、selector 或终点，各记录保留。另列 [尚缺模式路径的 '+format(sum(unresolved.values()),',')+' 个候选](unresolved/README.md)。\n\n',
                '## 怎样读一条命令\n\n',
                '例如 `(config-router)# priority <number:0..127> <cr>`：提示符标明解析模式，`priority` 是关键词，`<number:0..127>` 表示参数范围，`<cr>` 表示路径到达终止动作。参数记号按实际值替换，`<cr>` 对应回车。`<opaque:…>` 及其他 `<?…>` 表示未解析步骤，其实际输入含义保留未知；动态范围按记录原样展示。\n\n',
                '模式页中，**命令文本（txt）**直接列出命令和来源编号；**参数与证据（md）**逐条给出 handler、selector、EOL 和参数提示。条件、状态效果、缺口及注册关系链接到共享参考页。编号可用于定位原 gzip 目录中的 `evidence_id`。先列关键词开头的路径，带分析记号的前缀路径附后，各组按语法排序；每页最多 400 条，并限制 UTF-8 字节数。\n\n',
                '这份目录描述特定样本的候选语法与历史连接。当前注册、权限、谓词状态和实际执行分别依赖对应证据。命令是否 documented/undocumented 需要与适用版本文档对照，未逐条作该分类。\n\n',
                '## 证据模型\n\n','| 模型 | 路径记录 | 含义 |\n|---|---:|---|\n']
            for model,(description,_) in MODELS.items():intro.append('| '+model+' | '+format(counts[model],',')+' | '+description+' |\n')
            intro.extend(['\n基础模式和补充模式分开保存。条件安装模型保留注册调用、槽位、创建点、顺序和解析条件；当前生效情况另按运行时状态核对。跨捕获的映像关系通过 MD5/RVA 对齐，历史堆地址保持所属捕获来源。\n\n',
                '[条件与字段说明](evidence/README.md) · [版本分析结果](../README.md) · [原始派生目录](../cli/summary.json) · [后续模型统计](../unbound-cli/path-summary.json)\n\n',
                '## 按模式阅读\n\n','模式名称按采集结果保留，同根别名、父模式和定义候选见各模式页。全局配置从 configure 进入；接口配置从 interface/subinterface 进入；router、bgp-address-family 等为补充子模式入口。\n\n',
                '| 模式主名称 | 路径记录 |\n|---|---:|\n'])
            for mode,directory,count in mode_index:intro.append('| ['+label(mode)+']('+directory+'/README.md) | '+format(count,',')+' |\n')
            intro.extend(['\n## 来源与重建\n\n','输入文件与输出文本的 SHA256 记录在 [manifest.json](manifest.json)。生成器保留每条来源编号，分页和参考 ID 由内容确定。仓库根目录运行：\n\n',
                fenced('python tools/export_cli_textbook.py --version analysis/c8000v-26.01.02 --output analysis/c8000v-26.01.02/commands'),
                '\n当前路径图仍有未知动作、缺页及尚未关联的片段。节点图继续保存其他未选为代表路径的写法；此处按已导出的见证列出命令。\n'])
            write('README.md',''.join(intro))
            manifest={'schema_version':1,'identity':identity,'source_sha256':hashes,'source_records':dict(counts),
                'exported_witnesses':exported,'mode_primary_names':len(mode_index),'unique_eol_references':len(unique_eols),
                'unresolved_candidates':dict(unresolved),'command_pages':command_pages,'reference_pages':len(reference_pages),
                'page_max_utf8_bytes':max_bytes,'page_max_entries':400,
                'atom_records':db.execute('SELECT COUNT(*) FROM atoms').fetchone()[0],
                'sequence_records':db.execute('SELECT COUNT(*) FROM chains').fetchone()[0],
                'generator_sha256':digest(Path(__file__).read_bytes()),'artifact_sha256':written,
                'scope':'All input witnesses preserved with evidence IDs; no new CLI/runtime verification; no undocumented classification'}
            (output/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            for relative in old.keys()-written.keys():
                obsolete=(output/relative).resolve();obsolete.relative_to(output)
                if obsolete.is_file():obsolete.unlink()
            print(packed({k:v for k,v in manifest.items() if k not in ('artifact_sha256','source_sha256')}),flush=True)
            return manifest
        finally:db.close()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--version',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--max-page-bytes',type=int,default=196608)
    a=p.parse_args()
    if not 16384<=a.max_page_bytes<=524288:p.error('Page budget must be 16384..524288 UTF-8 bytes')
    build_book(a.version,a.output,a.max_page_bytes)


if __name__=='__main__':main()
