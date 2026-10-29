// Run the generated report's actual filtering script against all saved table rows.
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const html=fs.readFileSync(process.argv[2],'utf8');
const body=html.match(/<table id="fsm">[\s\S]*?<tbody>([\s\S]*?)<\/tbody>/)[1];
const rows=[...body.matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(m=>({textContent:m[1].replace(/<[^>]*>/g,' '),hidden:false}));
const search={value:'',addEventListener:(name,fn)=>{search[name]=fn;}};
const count={textContent:''};
const document={querySelectorAll:()=>rows,querySelector:s=>s==='#search'?search:count};
vm.runInNewContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],{document});
assert.equal(rows.length,224);assert.equal(count.textContent,'224 / 224 个表项');
for(const q of ['未知','D51AF30','WAIT_SWITCHOVER','no-such-ehsa-evidence']){
 search.value=q;search.input();
 const expected=rows.filter(r=>r.textContent.toLowerCase().includes(q.toLowerCase())).length;
 assert.equal(rows.filter(r=>!r.hidden).length,expected);
 assert.equal(count.textContent,expected+' / 224 个表项');
}
console.log('EHSA reader: all 224 cells, unknowns, callback search and empty results verified.');
