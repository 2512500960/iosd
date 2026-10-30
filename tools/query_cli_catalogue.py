"""Query a versioned CLI evidence catalogue without IDA or original Cisco files."""
import argparse,gzip,json
from pathlib import Path


def iter_matches(path,mode=None,contains=None):
    opener=gzip.open if str(path).endswith('.gz') else open
    with opener(path,'rt',encoding='utf-8') as stream:
        for line in stream:
            row=json.loads(line)
            if mode and row.get('mode')!=mode and mode not in row.get('mode_aliases',[]):continue
            if contains and contains.lower() not in row.get('syntax_candidate','').lower():continue
            yield row


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('catalogue',type=Path)
    p.add_argument('--mode');p.add_argument('--contains');p.add_argument('--limit',type=int,default=20)
    p.add_argument('--json',action='store_true');a=p.parse_args()
    if not 1<=a.limit<=10000:p.error('--limit must be 1..10000')
    for index,row in enumerate(iter_matches(a.catalogue,a.mode,a.contains)):
        if index>=a.limit:break
        if a.json:print(json.dumps(row,ensure_ascii=False))
        else:
            handler=row['handler'];location=('RVA '+hex(handler['rva'])) if handler['space']=='image' else 'captured VA '+hex(handler['va'])
            print('(%s)# %s | %s | selector=%s | conditions=%d | gaps=%d | %s'%
                  (row['prompt'],row['syntax_candidate'],location,row['selector_candidate'],len(row['conditions']),len(row['gaps']),row['evidence_id']))


if __name__=='__main__':main()
