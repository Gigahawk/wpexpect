from time import sleep
import os
import sys

import wpexpect

_runenv = os.environ.copy()
_runenv["TERM"] = "dumb"
_runenv["NO_COLOR"] = "1"
_runenv["PS1"] = ">"


def test_ctrl_c_unix():
    if sys.platform == "win32":
        return

    child = wpexpect.spawn("bash --norc")
    child.sendline("sleep 10")
    sleep(0.1)
    child.sendcontrol("c")
    child.expect(r"\^C", timeout=3)
    child.sendline("exit")
    child.wait()
