"""Measure an original ELF64 file offline; export layout metadata, not Cisco code or memory."""
import argparse,json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from iosd_helper.elf_layout import inspect_elf_layout


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('elf')
    p.add_argument('--expected-md5');p.add_argument('--output',required=True)
    a=p.parse_args();result=inspect_elf_layout(a.elf,a.expected_md5)
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'identity':result['identity'],'sections':len(result['sections']),
                      'file_buckets':result['file_buckets'],'load_summary':result['load_summary']}))


if __name__=='__main__':main()
