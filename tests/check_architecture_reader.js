// Execute the actual reader script in an offline minimal DOM; no browser/network.
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const html=fs.readFileSync(process.argv[2],'utf8');
const source=html.match(/<script>\s*([\s\S]*?)<\/script>/)[1];
class Element{
 constructor(text='',dataset={}){this.textContent=text;this.dataset=dataset;this.hidden=false;this.value='';this.checked=true;this.listeners={};this.attributes={};}
 addEventListener(name,fn){this.listeners[name]=fn;}
 setAttribute(name,value){this.attributes[name]=value;}
}
const sections=Array.from(html.matchAll(/<section data-topic="([^"]+)"[^>]*>([\s\S]*?)<\/section>/g),m=>new Element(m[2].replace(/<[^>]+>/g,' '),{topic:m[1]}));
const nav=sections.map(()=>new Element());
const buttons=['all','file','protocol','config'].map(filter=>new Element('',{filter}));
const elements=new Map();const classes=new Set();
const get=id=>{if(!elements.has(id))elements.set(id,new Element());return elements.get(id)};
const document={querySelectorAll:selector=>selector==='section[data-topic]'?sections:selector==='button[data-filter]'?buttons:nav,
 getElementById:get,body:{classList:{toggle:(name,on)=>on?classes.add(name):classes.delete(name),remove:name=>classes.delete(name)}}};
vm.runInNewContext(source,{document});
assert.equal(sections.filter(s=>!s.hidden).length,10);
buttons[2].listeners.click();assert.equal(sections.filter(s=>!s.hidden).length,1);
assert.equal(sections.find(s=>!s.hidden).dataset.topic,'protocol');assert.equal(buttons[2].attributes['aria-pressed'],'true');
get('search').value='never-matching-query';get('search').listeners.input();assert.ok(sections.every(s=>s.hidden));assert.equal(get('empty').hidden,false);
get('reset').listeners.click();assert.ok(sections.every(s=>!s.hidden));assert.equal(get('cover').hidden,false);
get('search').value='NVGEN';get('search').listeners.input();const found=sections.filter(s=>!s.hidden).length;assert.ok(found>0&&found<10);
assert.equal(nav.filter(n=>!n.hidden).length,found);
get('details').checked=false;get('details').listeners.change();assert.ok(classes.has('hide-details'));
get('reset').listeners.click();assert.ok(!classes.has('hide-details'));assert.ok(get('details').checked);
console.log('Atlas route filtering, search, empty results, navigation, address details and reset passed offline.');
