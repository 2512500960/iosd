const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(process.argv[2]||'reports/runtime-comparison-20261029/index.html','utf8');
const packed=html.match(/<script id="path-data" type="application\/json">([\s\S]*?)<\/script>/)[1];
const script=html.match(/<\/script><script>([\s\S]*?)<\/script>/)[1];
class Element{
 constructor(){this.children=[];this.listeners={};this.value='';this.textContent='';this.open=false}
 append(...items){this.children.push(...items)}
 replaceChildren(...items){this.children=items}
 addEventListener(name,fn){this.listeners[name]=fn}
}
const ids={};for(const id of ['path-data','mode','query','gate','search','tree','count'])ids[id]=new Element();
ids['path-data'].textContent=packed;ids.mode.value='configure';
vm.runInNewContext(script,{document:{getElementById:id=>ids[id],createElement:()=>new Element()},console});
assert(ids.tree.children.length>0);assert(ids.count.textContent.includes('500'));
ids.query.value='service internal';ids.search.listeners.click();
assert(!ids.count.textContent.includes('匹配 0 条'));
function expand(node){if(node.listeners.toggle){node.open=true;node.listeners.toggle()}for(const child of node.children)expand(child)}
expand(ids.tree);
function text(node){return node.textContent+' '+node.children.map(text).join(' ')}
assert(text(ids.tree).includes('internal'));
ids.query.value='';ids.mode.value='';ids.gate.value='blocked_by_observed_keyword_gate';ids.gate.listeners.change();
assert(!ids.count.textContent.includes('匹配 0 条'));
expand(ids.tree);assert(text(ids.tree).includes('当前直接门控拒绝'));
ids.query.value='impossible-query-no-command-4b8a';ids.search.listeners.click();
assert(ids.count.textContent.includes('匹配 0 条'));assert.strictEqual(ids.tree.children.length,0);
console.log('Runtime report filters, lazy tree, gate annotations and empty state passed.');
