"""Resumable bounded literal windows; unread regions and unfinished work stay explicit."""
import re

from .memory import MemoryReadError


PRINTABLE = re.compile(rb'(?<![\x20-\x7e])[\x20-\x7e]{3,2048}\x00')


def literal_windows(read, segments, query, cursor=None, max_bytes=64*1024*1024,
                    max_hits=2000, cancelled=lambda:False):
    """Resume even inside a hit-filled window. Cursor positions are captured EAs.

    One preceding byte suppresses fragments of a previously emitted string, and
    lookahead keeps strings crossing payload boundaries intact. A budget too
    small for the next window reports the required minimum without skipping it.
    """
    if max_bytes < 0 or max_hits < 1:raise ValueError('Invalid literal scan budget')
    state=dict(cursor or {'segment':0,'start':None,'after':0,'payload':0})
    if not 0 <= state['segment'] <= len(segments) or state['after']<0:
        raise ValueError('Invalid literal cursor segment/offset')
    rows=[];faults=[];ranges=[];attempted=0;loaded=0
    flags={'byte_limit_reached':False,'hit_limit_reached':False,'cancelled':False}
    needle=query.encode('ascii').lower()
    while state['segment'] < len(segments):
        segment=segments[state['segment']]
        start=segment['address'] if state['start'] is None else state['start']
        if not segment['address'] <= start <= segment['end']:raise ValueError('Literal cursor outside its segment')
        if start==segment['end']:
            state={'segment':state['segment']+1,'start':None,'after':0,'payload':0};continue
        if cancelled():flags['cancelled']=True;break
        payload=state['payload'] or min(65536,segment['end']-start)
        if not 1 <= payload <= min(65536,segment['end']-start):raise ValueError('Invalid literal cursor payload')
        read_start=max(segment['address'],start-1)
        size=min(start+payload+2048,segment['end'])-read_start
        if state['after']>size:raise ValueError('Literal cursor offset exceeds its window')
        state.update(start=start,payload=payload)
        if max_bytes-attempted < size:
            flags['byte_limit_reached']=True;flags['minimum_next_read_bytes']=size;break
        attempted+=size
        try:
            data=read(read_start,size)
            if len(data)!=size:raise MemoryReadError('Literal reader returned a short block')
        except MemoryReadError as exc:
            faults.append({'ea':read_start,'size':size,'error':str(exc)})
            state={'segment':state['segment'],'start':start+payload,'after':0,'payload':0};continue
        loaded+=len(data)
        ranges.append({'start_ea':read_start,'end_ea':read_start+size,'segment':segment['name']})
        owner_start=start-read_start;owner_end=owner_start+payload
        for i,match in enumerate(PRINTABLE.finditer(data)):
            if match.start() < max(owner_start,state['after']):continue
            if match.start() >= owner_end:break
            if i%64==0 and cancelled():
                state['after']=match.start();flags['cancelled']=True;break
            state['after']=match.end()
            if needle not in match[0].lower():continue
            rows.append({'ea':read_start+match.start(),'text':match[0][:-1].decode('ascii')})
            if len(rows)>=max_hits:flags['hit_limit_reached']=True;break
        if flags['cancelled'] or flags['hit_limit_reached']:break
        state={'segment':state['segment'],'start':start+payload,'after':0,'payload':0}
    return {'rows':rows,'faults':faults,'cursor':state if state['segment'] < len(segments) else None,
            'coverage':{'bytes_attempted':attempted,'bytes_read':loaded,'scanned_ranges':ranges,**flags},
            'scope':'NUL-terminated printable strings of 3..2048 bytes in selected IDB segments; encoded/longer strings are outside this scan'}
