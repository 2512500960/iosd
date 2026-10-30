"""Offline ELF64 container layout. No execution, raw code export or ownership inference."""
import hashlib
from pathlib import Path
import struct


def inspect_elf_layout(path, expected_md5=None):
    path = Path(path);size = path.stat().st_size
    md5 = hashlib.md5();sha = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8*1024*1024), b''):
            md5.update(block);sha.update(block)
        if expected_md5 and md5.hexdigest().lower() != expected_md5.lower():
            raise ValueError('ELF MD5 differs from expected sample')
        def read(offset, length):
            if offset < 0 or length < 0 or offset+length > size:
                raise ValueError('ELF table or section outside file')
            stream.seek(offset);raw = stream.read(length)
            if len(raw) != length:raise ValueError('Short ELF file read')
            return raw
        header = read(0,64)
        if header[:5] != b'\x7fELF\x02' or header[5] not in (1,2) or header[6] != 1:
            raise ValueError('Expected ELF64 version 1, little or big endian')
        order = '<' if header[5] == 1 else '>'
        kind,machine,version,entry,phoff,shoff,flags,ehsize,phsize,phnum,shsize,shnum,strindex = struct.unpack_from(order+'HHIQQQIHHHHHH',header,16)
        if version != 1 or ehsize < 64 or ehsize > size:raise ValueError('Invalid ELF header')
        def section(index):
            return struct.unpack(order+'IIQQQQIIQQ',read(shoff+index*shsize,64))
        if shoff:
            if shsize < 64:raise ValueError('Invalid section header size')
            zero = section(0)
            if shnum == 0:shnum = zero[5]
            if strindex == 0xffff:strindex = zero[6]
            if phnum == 0xffff:phnum = zero[7]
            if not 1 <= shnum <= 65536 or strindex >= shnum:raise ValueError('Invalid section table count/index')
            if shoff+shnum*shsize > size:raise ValueError('Section table outside file')
        elif shnum or strindex or phnum == 0xffff:
            raise ValueError('Missing section table')
        if phnum and (phsize < 56 or phnum > 65536):raise ValueError('Invalid program header size/count')
        if phnum and phoff+phnum*phsize > size:raise ValueError('Program table outside file')
        names = b''
        if shoff and strindex:
            name_section = section(strindex)
            if name_section[1] != 3 or name_section[5] > 8*1024*1024:
                raise ValueError('Invalid or excessive section-name table')
            names = read(name_section[4],name_section[5])
        sections=[];buckets={};spans=[]
        for index in range(shnum):
            name,typ,attrs,va,offset,length,link,info,align,entsize = section(index)
            if names:
                end=names.find(b'\0',name)
                if name >= len(names) or end < 0:raise ValueError('Invalid section name offset/termination')
                label=names[name:end].decode('utf-8','replace')
            else:label='section_%d'%index
            allocated=bool(attrs&2);nobits=typ==8
            # Section zero contains extended counts, not file or memory payload.
            file_bytes=length if typ not in (0,8) else 0
            if file_bytes:
                if offset+file_bytes > size:raise ValueError('Section payload outside file')
                spans.append((offset,offset+file_bytes,label))
            category=('executable' if attrs&4 else 'writable_data' if attrs&1 else 'readonly_data') if allocated else 'nonallocated_metadata'
            if nobits:category='nobits'
            buckets[category]=buckets.get(category,0)+file_bytes
            sections.append({'index':index,'name':label,'type':typ,'flags':attrs,'address':va,
                             'file_offset':offset,'size':length,'file_bytes':file_bytes,
                             'allocated':allocated,'executable':bool(attrs&4),'writable':bool(attrs&1),
                             'category':category,'nobits':nobits,'link':link,'entry_size':entsize})
        overlaps=[];last_end=0;last_name=None
        for start,end,label in sorted(spans):
            if start < last_end:overlaps.append({'section':label,'previous':last_name})
            if end > last_end:last_end,last_name=end,label
        if not overlaps:buckets['headers_tables_padding_and_unassigned']=size-sum(buckets.values())
        programs=[]
        for index in range(phnum):
            typ,attrs,offset,va,pa,filesz,memsz,align=struct.unpack(order+'IIQQQQQQ',read(phoff+index*phsize,56))
            if filesz and offset+filesz > size:raise ValueError('Segment payload outside file')
            if typ==1 and memsz < filesz:raise ValueError('PT_LOAD memory size smaller than file size')
            programs.append({'index':index,'type':typ,'flags':attrs,'file_offset':offset,
                             'address':va,'file_size':filesz,'memory_size':memsz,'alignment':align,
                             'permissions':''.join(c if attrs&b else '-' for c,b in [('R',4),('W',2),('X',1)])})
    loads=[p for p in programs if p['type']==1]
    return {'schema_version':1,'kind':'elf_layout','source':'original_elf_file',
            'identity':{'input_md5':md5.hexdigest(),'sha256':sha.hexdigest(),'file_name':path.name,
                        'file_size':size,'bits':64,'byteorder':'little' if order=='<' else 'big','machine':machine,'type':kind},
            'entry_elf_va':entry,'sections':sections,'program_headers':programs,
            'file_buckets':buckets,'section_overlaps':overlaps,
            'load_summary':{'file_bytes_sum':sum(p['file_size'] for p in loads),
                            'memory_bytes_sum':sum(p['memory_size'] for p in loads),
                            'address_span':max((p['address']+p['memory_size'] for p in loads),default=0)-min((p['address'] for p in loads),default=0)},
            'limits':['ELF64 container metadata only; does not assign protocol or component ownership',
                      'ELF virtual addresses are not current runtime VAs; ET_DYN needs a verified load bias',
                      'NOBITS has no file payload; virtual reservation and PT_LOAD sums are not resident memory',
                      'File buckets are additive only if section_overlaps is empty; gaps include ELF header tables and padding']}
