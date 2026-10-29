"""Copy this file AND the iosd_helper package into IDA's user plugins folder."""
import os
import sys

_root = os.path.dirname(os.path.abspath(__file__))
if _root not in sys.path:
    sys.path.insert(0, _root)

import ida_idaapi
from iosd_helper.ui import Application


class IosdModule(ida_idaapi.plugmod_t):
    def __init__(self):
        super().__init__()
        self.application = Application()

    def run(self, arg):
        self.application.guard(self.application.menu)

    def __del__(self):
        self.application.close()


class IosdPlugin(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_MULTI
    comment = "Explore iosd static structures and runtime memory"
    help = "See iosd_helper README.md"
    wanted_name = "iosd Helper"
    wanted_hotkey = "Alt-Shift-I"

    def init(self):
        return IosdModule()


def PLUGIN_ENTRY():
    return IosdPlugin()
