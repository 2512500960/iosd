import unittest

from iosd_helper.lifecycle import analyze_lifecycle, variants
from iosd_helper.cached_ir import expression, lower_cached_function
from iosd_helper.addressing import ImageCoordinates


def reference(ea,function=False):return {"kind":"global","ea":ea,"rva":ea,"is_function":function}
def address(ea):return {"kind":"ref","arg":reference(ea)}
def call(target,*args):return {"kind":"call","target":target,"args":list(args)}
def event(kind,order=1,**fields):return {"kind":kind,"order":order,"site_rva":None,"guards":[],**fields}
def function(ea,*events):return {"rva":ea,"events":list(events)}
def inputs(functions,**extra):
    capture={"identity":{"input_md5":"abc","imagebase":0},"functions":functions,**extra}
    graph={"identity":{"input_md5":"abc","imagebase":0},"graph":{"nodes":[{"address":0x2000,"handler_candidate":0x1000,"selector_candidate":7}]}}
    profile={"input_md5":"abc","apis":[{"rva":0x5000,"role":"register_table","table_arg":0,"evidence":"fixture"},
                                            {"rva":0x6000,"role":"create_link","type":1,"key_arg":0,"root_arg":2,"evidence":"fixture"}]}
    return capture,graph,profile


class LifecycleTests(unittest.TestCase):
    def test_generic_api_arguments_and_handler_group(self):
        c,g,p=inputs([function(0x1000,event("call",target=0x5000,args=[address(0x3000)]),
                              event("call",2,target=0x6000,args=[address(0x30),{"kind":"number","value":0},address(0x4000)]))])
        r=analyze_lifecycle(c,g,p)
        self.assertEqual(r["registrations"][0]["tables"],[0x3000])
        self.assertEqual(r["dynamic_links"][0]["anchors"],[0x4000])
        self.assertIsNone(r["dynamic_links"][0]["heap_address"])
        self.assertEqual(r["trigger_candidates"][0]["commands"][0]["selector"],7)
        self.assertFalse(r["trigger_candidates"][0]["feasibility_verified"])

    def test_indirect_getter_binding_through_local_alias_is_only_candidate(self):
        getter=call(0x8000)
        lhs={"kind":"deref","arg":getter}
        consumer=event("call",2,target=None,target_expression={"kind":"deref","arg":{"kind":"var","index":1}},args=[])
        c,g,p=inputs([function(0x1000,event("assignment",left={"kind":"var","index":1},right=getter),consumer),
                     function(0x7000,event("assignment",left=lhs,right=reference(0x9000,True))),
                     function(0x9000,event("call",target=0x5000,args=[address(0x3000)]))])
        r=analyze_lifecycle(c,g,p)
        self.assertEqual(len(r["bindings"]),1)
        self.assertEqual(r["indirect_calls"][0]["binding_candidates"][0]["target"],0x9000)
        self.assertEqual(r["trigger_candidates"][0]["call_chain"][0]["kind"],"indirect_binding_candidate")

    def test_multiple_local_definitions_and_unresolved_api_arguments_preserved(self):
        c,g,p=inputs([function(0x1000,event("assignment",left={"kind":"var","index":1},right=address(0x3000)),
                              event("assignment",2,left={"kind":"var","index":1},right=address(0x4000)),
                              event("call",3,target=0x5000,args=[{"kind":"var","index":1}]),
                              event("call",4,target=0x5000,args=[{"kind":"unknown","reason":"opaque"}]))])
        r=analyze_lifecycle(c,g,p)
        self.assertEqual(r["registrations"][0]["tables"],[0x3000,0x4000])
        self.assertEqual(len(r["registrations"]),2)
        self.assertFalse(r["registrations"][1]["arguments_resolved"])

    def test_state_dependency_and_pending_functions_are_visible(self):
        c,g,p=inputs([function(0x1000,event("global_access",global_rva=0x88,access="write")),
                     function(0x9000,event("global_access",global_rva=0x88,access="read",in_guard=True))],pending_functions=[0x777])
        r=analyze_lifecycle(c,g,p)
        self.assertEqual(r["state_dependencies"][0]["kind"],"write_may_affect_guard")
        self.assertTrue(any(x.get("function")==0x777 for x in r["unknown"]))

    def test_unacquired_registration_call_remains_trigger_candidate(self):
        c,g,p=inputs([],api_xrefs=[{"caller":0x1000,"callee":0x5000,"site_rva":0x1010}])
        r=analyze_lifecycle(c,g,p)
        self.assertEqual(len(r["registrations"]),1)
        self.assertEqual(r["registrations"][0]["tables"],[])
        self.assertEqual(len(r["trigger_candidates"]),1)
        self.assertTrue(r["unknown"])

    def test_identity_and_different_capture_bases(self):
        c,g,p=inputs([function(0x1000,event("call",target=0x5000,args=[address(0xA000)]))])
        c["identity"]["imagebase"]=0x7000
        r=analyze_lifecycle(c,g,p)
        self.assertEqual(r["registrations"][0]["tables"],[0x3000])
        c["identity"]["input_md5"]="different"
        with self.assertRaisesRegex(ValueError,"MD5"):analyze_lifecycle(c,g,p)

    def test_cached_expression_retains_unsupported_and_parses_pointer_assignment(self):
        expr=expression('*(_QWORD *)(sub_8000() & 0x7FFFFFFFFFFFFFFFLL)')
        self.assertEqual(expr["kind"],"deref")
        self.assertEqual(expression('weird->member ? a : b')["kind"],"unknown")
        source={"address":0x1000,"input_md5":"abc","imagebase":0,"code":'''void sub_1000() {
  v1 = sub_8000();
  *(_QWORD *)(sub_8000() & 0x7FFFFFFFFFFFFFFFLL) = _byteswap_uint64((unsigned __int64)sub_9000);
  if ( !byte_88 ) { sub_5000((__int64)(&off_3000 + 0x8000000000000000LL), 0); }
}'''}
        f=lower_cached_function(source)
        c,g,p=inputs([f]);r=analyze_lifecycle(c,g,p)
        self.assertEqual(r["registrations"][0]["tables"],[0x3000])
        self.assertEqual(len(r["bindings"]),1)
        self.assertTrue(r["registrations"][0]["guards"])

    def test_typed_coordinates_never_double_rebase_and_stale_mapping_rejected(self):
        mapping=ImageCoordinates("abc",0,0x70000000,0x70000000)
        self.assertEqual(mapping.reference(0x1234)["runtime_va"],0x70001234)
        mapping.assert_current({"input_md5":"abc","imagebase":0x70000000})
        with self.assertRaisesRegex(ValueError,"changed"):
            mapping.assert_current({"input_md5":"abc","imagebase":0x71000000})
        with self.assertRaises(ValueError):mapping.rva(-1)
        with self.assertRaises(ValueError):ImageCoordinates("abc",0,0).runtime_va(1)

    def test_variant_bound_retains_explicit_unknown_marker(self):
        alternatives={"kind":"alternatives","values":[{"kind":"number","value":i} for i in range(8)]}
        values=variants({"kind":"binary","op":"add","left":alternatives,"right":alternatives},limit=4)
        self.assertTrue(any(v.get("kind")=="unknown" for v in values))

    def test_cached_compound_state_update_is_read_and_write(self):
        f=lower_cached_function({"address":0x1000,"code":"void sub_1000() { byte_88 |= 1; }"})
        self.assertEqual({e["access"] for e in f["events"] if e["kind"]=="global_access"},{"read","write"})
