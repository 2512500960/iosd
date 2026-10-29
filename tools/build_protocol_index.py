"""Derive a portable subsystem search index from a reviewed saved architecture map."""
import argparse
import hashlib
import json
from pathlib import Path


def build(source, destination):
    raw = source.read_bytes();model = json.loads(raw)
    if model.get('kind') != 'iosd_architecture_map' or model.get('address_space') != 'rva':
        raise ValueError('Expected a reviewed RVA architecture map')
    rows = [{key:row[key] for key in ('name','record_rva','init_rva','category')} for row in model['subsystems']]
    result = {'schema_version':1, 'kind':'protocol_subsystem_index', 'input_md5':model['input_md5'],
              'address_space':'rva', 'source_sha256':hashlib.sha256(raw).hexdigest(), 'subsystems':rows,
              'scope':'Saved metadata candidates for this input; names/categories/init RVAs do not prove packet handlers or runtime activation'}
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    return len(rows)


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);p.add_argument('output',type=Path)
    args=p.parse_args();print('Indexed',build(args.source,args.output),'subsystem metadata candidates')
