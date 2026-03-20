import sys
import os

import wpexpect


def test_print_system():
    print(f"RUNNING ON PLATFORM: {sys.platform}")


_runenv = os.environ.copy()
_runenv["PS1"] = "GO:"


# Borrowed from pexpect test_run.py, test_run_event_as_string
def test_run():
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
