"""Version-independent search keys, never historical absolute addresses."""
import re


def symbol_kind(name):
    name = name.lstrip(".")
    if "_message_dispatch_init" in name:
        return "message registration candidate"
    if "_message_handler" in name:
        return "message handler name"
    if "mqipc" in name:
        return "MQIPC name"
    if name.startswith("tbl_"):
        return "data model name (field boundaries unresolved)"
    if "parse_func" in name or "parser_add" in name or re.search(r"(?:^|_)icm_", name):
        return "CLI/parser name"
    return None


KEY_NAMES = (
    "icm_main", "icm_print_cli_tree", "icm_add_node_to_parse_tree",
    "icm_add_cli_str_to_parser_tree", "icm_check_and_create_diff_tree",
    "parser_add_command", "parse_cmd", "subsys_find_by_name",
    "vty_mgt_vty_req_message_handler", "__be_wsman_iosd_init_mqipc",
    "CRFT_func",
)

ANCHORS = {
    "icm_main literal": b"icm_main\0",
    "icm_print_cli_tree literal": b"icm_print_cli_tree\0",
    "icm_add_node_to_parse_tree literal": b"icm_add_node_to_parse_tree\0",
    "FRR manager registration diagnostic (not function identity)": b"Unable to parser_add_command",
    "KRON parse_cmd wrapper trace": b"Call parse_cmd '",
    "ICM node allocation": b"First Node allocated: %p level:%d line:%s",
    "ICM node print": b"Node:%p Level:%d Flags:0x%x",
    "diff temporary root trace": b"Generate CLI command is_old:%d root_cli:%p",
    "subsystem lookup assertion": b'subsys_find_by_name("generic_atom")',
}


def literal_matches(data, start, primary_size, needles=ANCHORS):
    """Overlapping chunks: only own matches starting in the primary chunk."""
    result = []
    for label, needle in needles.items():
        pos = data.find(needle)
        while pos >= 0 and pos < primary_size:
            result.append({"address": start + pos, "anchor": label,
                           "matched_text": needle.rstrip(b"\0").decode("ascii"),
                           "evidence": "literal bytes; direct references are candidates, not proof of function identity"})
            pos = data.find(needle, pos + 1)
    return result
