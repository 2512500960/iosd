"""Run via IDA File > Script file (Alt+F7). Re-run to reload development code.

Do not simultaneously install the plugin while developing with this loader.
"""
import builtins
import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
if root not in sys.path:
    sys.path.insert(0, root)

previous = getattr(builtins, "_iosd_helper_dev", None)
if previous is not None:
    previous.close()
    del builtins._iosd_helper_dev

for name in list(sys.modules):
    if name == "iosd_helper" or name.startswith("iosd_helper."):
        del sys.modules[name]

from iosd_helper.ui import Application

builtins._iosd_helper_dev = Application()
builtins._iosd_helper_dev.guard(builtins._iosd_helper_dev.menu)
