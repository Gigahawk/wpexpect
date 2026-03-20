import sys
import os

import wpexpect


def test_print_system():
    print(f"RUNNING ON PLATFORM: {sys.platform}")


_runenv = os.environ.copy()
_runenv["PS1"] = "Microsoft>"


# Borrowed from pexpect/wexpect test_run.py, test_run_event_as_string
def test_run_event_as_string():
    if sys.platform == "win32":
        shell = "cmd"
        le = "\r\n"
    else:
        shell = "bash --norc"
        le = "\n"
    events = {
        # second match on 'abc', echo 'def'
        "abc.*>": f'echo "def"{le}',
        # final match on 'def': exit
        "def.*>": f"exit{le}",
        # first match on 'GO:' prompt, echo 'abc'
        "Microsoft.*>": f'echo "abc"{le}',
    }

    (_, exitstatus) = wpexpect.run(
        shell, withexitstatus=True, events=events, env=_runenv, timeout=10
    )
    assert exitstatus == 0
