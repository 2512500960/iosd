"""Conservative IR candidates from cached Hex-Rays text, for offline work.

This is a bounded expression subset, not a C parser. Unsupported expressions
keep original text. Sites are source offsets, never invented instruction EAs.
Use structured IDA acquisition for precise instruction/condition association.
"""
import re


TOKEN = re.compile(r'\s*(0x[0-9a-fA-F]+(?:[uUlL]*)|\d+(?:[uUlL]*)|[A-Za-z_]\w*|==|!=|<=|>=|&&|\|\||<<|>>|[()\[\].,+*/&|^!~<>-])')
GLOBAL = re.compile(r'(?:unk|byte|word|dword|qword|off|xmmword|stru)_([0-9a-fA-F]+)$')
FUNCTION = re.compile(r'sub_([0-9a-fA-F]+)$')
TYPES = {"unsigned", "signed", "__int64", "__int32", "__int16", "__int8", "int", "char", "short", "long", "void", "const", "_QWORD", "_DWORD", "_WORD", "_BYTE", "_UNKNOWN", "*"}
PRECEDENCE = {"||":1,"&&":2,"|":3,"^":4,"&":5,"==":6,"!=":6,"<":7,">":7,"<=":7,">=":7,"<<":8,">>":8,"+":9,"-":9,"*":10,"/":10}
OPS = {"|":"or","&":"and","^":"xor","+":"add","-":"sub","*":"mul","==":"eq","!=":"ne","<":"lt",">":"gt","<=":"le",">=":"ge","&&":"logical_and","||":"logical_or","<<":"shl",">>":"shr","/":"div"}


def expression(text, base=0):
    text = text.strip()
    tokens, position = [], 0
    while position < len(text):
        match = TOKEN.match(text, position)
        if not match:
            return {"kind":"unknown","reason":"unsupported cached C expression","text":text}
        tokens.append(match.group(1))
        position = match.end()
        if len(tokens) > 512:
            return {"kind":"unknown","reason":"cached expression token bound","text":text}
    index = 0
    def parse(minimum=0, depth=0):
        nonlocal index
        if depth > 32 or index >= len(tokens):
            raise ValueError("expression nesting/end")
        token = tokens[index]; index += 1
        if token == "(":
            end = index
            while end < len(tokens) and tokens[end] in TYPES:
                end += 1
            if end > index and end < len(tokens) and tokens[end] == ")":
                index = end + 1
                left = {"kind":"cast","arg":parse(11,depth+1)}
            else:
                left = parse(0,depth+1)
                if index >= len(tokens) or tokens[index] != ")":raise ValueError("unclosed group")
                index += 1
        elif token in ("*","&","!","~","-"):
            left = {"kind":{"*":"deref","&":"ref","!":"not","~":"bit_not","-":"neg"}[token],"arg":parse(11,depth+1)}
        elif re.fullmatch(r'(?:0x[0-9a-fA-F]+|\d+)[uUlL]*',token):
            left = {"kind":"number","value":int(re.sub(r'[uUlL]+$','',token),0) if not token.isdigit() else int(token)}
        elif GLOBAL.fullmatch(token) or FUNCTION.fullmatch(token):
            address = int((GLOBAL.fullmatch(token) or FUNCTION.fullmatch(token)).group(1),16)
            left = {"kind":"global","ea":address,"rva":address-base,"name":token,"is_function":bool(FUNCTION.fullmatch(token))}
        elif re.fullmatch(r'[A-Za-z_]\w*',token):
            left = {"kind":"var","index":token}
        else:
            raise ValueError("unsupported prefix")
        while index < len(tokens):
            op = tokens[index]
            if op == "(":
                index += 1; args = []
                if index < len(tokens) and tokens[index] != ")":
                    while True:
                        args.append(parse(0,depth+1))
                        if index < len(tokens) and tokens[index] == ",":index += 1
                        else:break
                if index >= len(tokens) or tokens[index] != ")":raise ValueError("unclosed call")
                index += 1
                target = left["rva"] if left.get("is_function") else None
                left = {"kind":"call","target":target,"target_expression":left,"args":args}
            elif op in PRECEDENCE and PRECEDENCE[op] >= minimum:
                index += 1
                left = {"kind":"binary","op":OPS[op],"left":left,"right":parse(PRECEDENCE[op]+1,depth+1)}
            else:
                break
        return left
    try:
        result = parse()
        if index != len(tokens):raise ValueError("unparsed suffix")
        return result
    except (ValueError, RecursionError):
        return {"kind":"unknown","reason":"unsupported cached C expression","text":text}


def close_pair(text, start, opening="(", closing=")"):
    depth = 0
    for index in range(start,min(len(text),start+20000)):
        if text[index] == opening:depth += 1
        elif text[index] == closing:
            depth -= 1
            if depth == 0:return index
    return None


def split_args(text):
    result, begin, depth = [], 0, 0
    for index,char in enumerate(text):
        if char in "([":depth += 1
        elif char in ")]":depth -= 1
        elif char == "," and depth == 0:
            result.append(text[begin:index]);begin=index+1
    if text.strip():result.append(text[begin:])
    return result


def lower_cached_function(evidence, max_events=5000):
    code, base, ea = evidence["code"], evidence.get("imagebase",0), evidence["address"]
    function = {"rva":ea-base,"capture_ea":ea,"name":evidence.get("name",""),"code":code,
                "evidence_source":"cached_decompiler_text_candidates","source_file":evidence.get("source_file"),
                "identity_verified":evidence.get("identity_verified",False),"events":[],"path_conditions_complete":False,
                "source_truncated":evidence.get("_output_truncated",False),
                "limitations":["Bounded C expression subset; source offsets are not instruction addresses.","All control-flow/alias relations remain candidates; unsupported source preserved."]}
    # Generated address-based names cannot be trusted after a rebase. Require
    # structured ctree acquisition in that situation instead of guessing.
    if base != 0:
        function["error"] = "cached generated names at nonzero imagebase need a symbol-address map; source retained"
        return function
    masked = re.sub(r'"(?:\\.|[^"\\])*"|/\*[\s\S]*?\*/|//[^\n]*',lambda m:" "*len(m.group()),code)
    body = masked.find("{")
    if body < 0:
        function["error"] = "cached function body missing"
        return function
    ranges = []
    for match in re.finditer(r'\bif\s*\(',masked[body:]):
        start = body + match.end()-1
        end = close_pair(masked,start)
        if end is None:continue
        statement = end+1
        while statement < len(masked) and masked[statement].isspace():statement+=1
        last = close_pair(masked,statement,"{","}") if statement<len(masked) and masked[statement]=="{" else masked.find(";",statement)
        if last is None or last<0:continue
        condition = expression(code[start+1:end],base)
        ranges.append((statement,last,{"kind":"if","expression":condition,"branch":"then","evaluated":False,"source_span":[start+1,end]}))
    def context(position):
        return {"site_rva":None,"source_offset":position,"guards":[r for first,last,r in ranges if first<=position<=last],
                "evidence_quality":"cached text candidate"}
    events = []
    for match in re.finditer(r'\bsub_([0-9a-fA-F]+)\s*\(',masked[body:]):
        start = body+match.start();begin=body+match.end()-1;end=close_pair(masked,begin)
        if end is None:continue
        args = [expression(arg,base) for arg in split_args(code[begin+1:end])]
        events.append({**context(start),"kind":"call","target":int(match.group(1),16)-base,"args":args})
    for match in re.finditer(r'^\s*([^;\n{}]+?)\s+=(?!=)\s*([^;]+);',masked[body:],re.M):
        start=body+match.start();left=code[body+match.start(1):body+match.end(1)];right=code[body+match.start(2):body+match.end(2)]
        events.append({**context(start),"kind":"assignment","left":expression(left,base),"right":expression(right,base)})
    # Common CRB function-pointer calls wrap a dereference in byte-swap helpers.
    for match in re.finditer(r'\b_byteswap_uint64\s*\(',masked[body:]):
        start=body+match.start();begin=body+match.end()-1;end=close_pair(masked,begin)
        if end is None:continue
        suffix=re.match(r'\s*\)*\s*\(',masked[end+1:])
        if not suffix:continue
        arg_begin=end+1+suffix.end()-1;arg_end=close_pair(masked,arg_begin)
        if arg_end is None:continue
        events.append({**context(start),"kind":"call","target":None,
                       "target_expression":expression(code[start:end+1],base),
                       "args":[expression(arg,base) for arg in split_args(code[arg_begin+1:arg_end])]})
    for match in re.finditer(r'\b(?:unk|byte|word|dword|qword|off|xmmword)_([0-9a-fA-F]+)\b',masked[body:]):
        start=body+match.start();after=masked[body+match.end():]
        before=masked[max(body,start-2):start]
        if before.rstrip().endswith("&"):continue
        compound=bool(re.match(r'\s*(?:[+|&^*/-]=|\+\+|--)',after))
        write=bool(re.match(r'\s*=(?!=)',after)) or compound
        events.append({**context(start),"kind":"global_access","global_rva":int(match.group(1),16)-base,
                       "name":match.group(),"access":"write" if write else "read",
                       "in_guard":any(r["source_span"][0]<=start<r["source_span"][1] for _,_,r in ranges),
                       "value_expression":None,"guard_membership_complete":False})
        if compound:
            events.append({**context(start),"kind":"global_access","global_rva":int(match.group(1),16)-base,
                           "name":match.group(),"access":"read","in_guard":False,
                           "value_expression":{"kind":"unknown","reason":"compound update value not evaluated"}})
    events.sort(key=lambda e:(e["source_offset"], e["kind"]!="assignment"))
    function["events"]=[{**event,"order":index+1} for index,event in enumerate(events[:max_events])]
    function["truncated"]=len(events)>max_events
    function["unsupported_expressions"]=sum(1 for event in function["events"] if "unsupported cached" in str(event))
    return function
