// Exercise the actual offline reader script; no browser, network or IDA access.
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const html=fs.readFileSync(process.argv[2],'utf8');
const script=html.match(/<script>\s*([\s\S]*?)<\/script>/)[1];
class Element{
  constructor(text=''){this.textContent=text;this.value='';this.hidden=false;this.dataset={};this.listeners={};this.attributes={};}
  addEventListener(name,fn){this.listeners[name]=fn;}
  setAttribute(name,value){this.attributes[name]=value;}
}
const plain=text=>text.replace(/<[^>]*>/g,' ').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
const sections=Array.from(html.matchAll(/<section class="chapter" data-chapter="([^"]+)">([\s\S]*?)<\/section>/g),m=>new Element(plain(m[2])));
const nav=sections.map(()=>new Element());
const elements=new Map();
const classes=new Set();
const body={classList:{toggle:name=>{if(classes.has(name)){classes.delete(name);return false;}classes.add(name);return true;},remove:name=>classes.delete(name)}};
const props={};const root={dataset:{},style:{setProperty:(name,value)=>props[name]=value}};
const document={documentElement:root,body,querySelectorAll:selector=>selector==='section.chapter'?sections:(selector==='li[data-nav]'?nav:[]),
  getElementById:id=>{if(!elements.has(id))elements.set(id,new Element());return elements.get(id);},createElement:()=>new Element()};
const storage=new Map();let scrolled=false;
vm.runInNewContext(script,{document,localStorage:{getItem:key=>storage.get(key)||null,setItem:(key,value)=>storage.set(key,value)},window:{scrollTo:()=>scrolled=true}});
const get=id=>elements.get(id);
assert.equal(sections.length,23);
get('search').value='NVGEN';get('search').listeners.input();
const expected=sections.filter(s=>s.textContent.toLowerCase().includes('nvgen')).length;
assert.ok(expected>0&&expected<23);assert.equal(sections.filter(s=>!s.hidden).length,expected);
assert.equal(nav.filter(s=>!s.hidden).length,expected);assert.ok(get('result-count').textContent.includes(String(expected)));
get('search').value='unmatched-textbook-query-!';get('search').listeners.input();assert.ok(sections.every(s=>s.hidden));
get('clear').listeners.click();assert.ok(sections.every(s=>!s.hidden));
for(let i=0;i<20;i++)get('larger').listeners.click();assert.equal(props['--reading-size'],'24px');
for(let i=0;i<20;i++)get('smaller').listeners.click();assert.equal(props['--reading-size'],'14px');
get('theme').listeners.click();assert.equal(root.dataset.theme,'dark');get('theme').listeners.click();assert.equal(root.dataset.theme,'light');
get('menu').listeners.click();assert.equal(get('menu').attributes['aria-expanded'],'true');
get('menu').listeners.click();assert.equal(get('menu').attributes['aria-expanded'],'false');
get('top').listeners.click();assert.ok(scrolled);
console.log('Reader chapter filtering, empty results, reset, font limits, theme, navigation and back-to-top passed.');
