import unittest

from iosd_helper.locators import literal_matches, symbol_kind


class LocatorTests(unittest.TestCase):
    def test_icm_name_requires_a_token_boundary(self):
        self.assertIsNone(symbol_kind("aRemovetrafficm_3"))
        self.assertEqual(symbol_kind("icm_main"), "CLI/parser name")
        self.assertEqual(symbol_kind(".__be_icm_main"), "CLI/parser name")

    def test_overlapping_chunks_have_one_owner(self):
        needles = {"anchor": b"parser\0"}
        raw = b"xxparser\0xxparser\0"
        first = literal_matches(raw, 0x1000, 8, needles)
        second = literal_matches(raw[8:], 0x1008, 8, needles)
        self.assertEqual([row["address"] for row in first + second], [0x1002, 0x100b])

    def test_all_occurrences_and_no_accidental_prefix(self):
        rows = literal_matches(b"icm_main_extra\0icm_main\0icm_main\0", 0, 128,
                               {"main": b"icm_main\0"})
        self.assertEqual([r["address"] for r in rows], [15, 24])


if __name__ == "__main__":
    unittest.main()
