// Exercise the generated catalogue's actual search and paging script without network dependencies.
const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
const html = fs.readFileSync(process.argv[2], 'utf8');
const payload = html.match(/<script id="catalogue-data" type="application\/json">([\s\S]*?)<\/script>/)[1];
const script = html.match(/<script>\r?\n([\s\S]*?)<\/script>/)[1];
class Element {
  constructor() { this.children=[]; this.value=''; this.textContent=''; }
  append(child) { this.children.push(child); if (!this.value && child.value) this.value=child.value; }
  replaceChildren() { this.children=[]; }
}
const elements = new Map();
const document = {
  getElementById(id) { if (!elements.has(id)) elements.set(id, new Element()); return elements.get(id); },
  createElement() { return new Element(); }
};
document.getElementById('catalogue-data').textContent=payload;
const context=vm.createContext({document,setTimeout:fn=>{fn();return 1;},clearTimeout:()=>{}});
vm.runInContext(script, context);
const data=JSON.parse(payload);
const primary=process.argv[4]||(data.tables.keywords?'keywords':(data.tables.paths?'paths':Object.keys(data.tables)[0]));
if (elements.get('kind').value!==primary) { elements.get('kind').value=primary; elements.get('kind').onchange(); }
const secondary=Object.keys(data.tables).find(key=>key!==primary);
const query=process.argv[3]||(data.tables.keywords?'exporter':'config');
assert.equal(elements.get('body').children.length, Math.min(200,data.tables[primary].length));
elements.get('query').value=query;
elements.get('query').oninput();
const expected=data.tables[primary].filter(row=>Object.values(row).some(value=>String(value??'').toLowerCase().includes(query)));
assert.ok(elements.get('count').textContent.startsWith(expected.length+' 条'));
if (expected.length) {
  elements.get('body').children[0].onclick();
  assert.deepEqual(JSON.parse(elements.get('details').textContent),expected[0]);
}
elements.get('query').value='';
elements.get('kind').value=secondary;
elements.get('kind').onchange();
assert.ok(elements.get('count').textContent.startsWith(data.tables[secondary].length+' 条'));
elements.get('kind').value=primary;
elements.get('kind').onchange();
if (data.tables[primary].length>200) {
  elements.get('next').onclick();
  elements.get('body').children[0].onclick();
  assert.deepEqual(JSON.parse(elements.get('details').textContent),data.tables[primary][200]);
}
elements.get('query').value='a-query-with-no-matching-iosd-record-!';
elements.get('query').oninput();
assert.equal(elements.get('body').children.length,0);
assert.equal(elements.get('next').disabled,true);
console.log('Catalogue search, type selection, pagination, details and empty results passed.');
