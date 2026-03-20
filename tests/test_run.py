import sys
import os
import re

import wpexpect


def test_print_system():
    print(f"RUNNING ON PLATFORM: {sys.platform}")


_runenv = os.environ.copy()
_runenv["PS1"] = "GO:"


# Borrowed from pexpect test_run.py, test_run_event_as_string
def test_run_unix():
    if sys.platform == "win32":
        return
    events = [
        # second match on 'abc', echo 'def'
        ("abc\r\n.*GO:", 'echo "def"\n'),
        # final match on 'def': exit
        ("def\r\n.*GO:", "exit\n"),
        # first match on 'GO:' prompt, echo 'abc'
        ("GO:", 'echo "abc"\n'),
    ]

    (_, exitstatus) = wpexpect.run(
        "bash --norc", withexitstatus=True, events=events, env=_runenv, timeout=10
    )
    assert exitstatus == 0


# Borrowed from wexpect test_run.py, test_run_event_as_string
def test_run_win():
    if sys.platform != "win32":
        return
    re_flags = re.DOTALL | re.MULTILINE
    events = {
        # second match on 'abc', echo 'def'
        re.compile("abc.*>", re_flags): 'echo "def"\r\n',
        # final match on 'def': exit
        re.compile("def.*>", re_flags): "exit\r\n",
        # first match on 'GO:' prompt, echo 'abc'
        re.compile("Microsoft.*>", re_flags): 'echo "abc"\r\n',
    }

    (data, exitstatus) = wpexpect.run(
        "cmd", withexitstatus=True, events=events, timeout=5
    )
    assert exitstatus == 0
