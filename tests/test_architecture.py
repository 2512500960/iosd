import unittest
from iosd_helper.architecture import build_architecture


class ArchitectureTests(unittest.TestCase):
    def fixture(self):
        identity = {"input_md5":"abc","imagebase":0x1000}
        static = {"identity":identity,"steps":[{"name":"subsystem_candidates_all_encodings","result":{"runs":[
            {"section":"subsys","pointer_mode":"little","rows":[{"name":"protocol_entity","address":0x1100,
             "init_candidate":0x1200,"raw_hex":(bytes(40)+b'\0\4'+bytes(14)).hex(),"status":"candidate"}]}]}}]}
        modules = {"identity":identity,"module_metadata":{"headers":[
            {"address":0x1300,"name":"level_protocol","field_10_candidate":0,"field_18_candidate":0},
            {"address":0x1320,"name":"worker","field_10_candidate":0x1500,"field_18_candidate":0x1510}],
            "links":[{"address":0x1400,"endpoint_a":0x1320,"endpoint_b":0x1300,"tag":0xabefabef}]}}
        profile={"input_md5":"abc","subsystem_pointer_mode":"little","subsystem_section":"subsys",
                 "categories":{"4":"Protocol"},"module_link_roles":{"0xabefabef":"member_of"}}
        return static,modules,profile

    def test_categories_and_module_groups_stay_separate_with_original_evidence(self):
        static,modules,profile = self.fixture()
        result = build_architecture(static,modules,profile)
        self.assertEqual(result["subsystems"][0]["category"],"Protocol")
        self.assertEqual(result["subsystems"][0]["init_rva"],0x200)
        self.assertNotIn("parent",result["subsystems"][0])
        self.assertEqual(result["modules"][0]["kind"],"group_node")
        self.assertEqual(result["modules"][1]["kind"],"callback_node")
        self.assertEqual(result["module_links"][0]["relation"],"member_of")
        self.assertEqual(result["subsystems"][0]["evidence"]["raw_hex"],static["steps"][0]["result"]["runs"][0]["rows"][0]["raw_hex"])

    def test_wrong_binary_rejected_and_unknown_link_retained(self):
        static,modules,profile=self.fixture()
        modules["identity"]={"input_md5":"other","imagebase":0}
        with self.assertRaises(ValueError):build_architecture(static,modules,profile)
        modules["identity"]=static["identity"]
        modules["module_metadata"]["links"][0]["endpoint_b"]=0x9999
        result=build_architecture(static,modules,profile)
        self.assertEqual(result["module_links"][0]["relation"],"unknown")
        self.assertEqual(result["module_links"][0]["b_rva"],0x8999)

    def test_ambiguous_encoding_is_not_silently_merged(self):
        static,modules,profile=self.fixture()
        runs=static["steps"][0]["result"]["runs"]
        runs.append(runs[0])
        with self.assertRaises(ValueError):build_architecture(static,modules,profile)


if __name__ == '__main__':unittest.main()
