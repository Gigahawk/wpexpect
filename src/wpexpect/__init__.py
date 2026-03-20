import sys

from pexpect import *  # noqa: F403

if sys.platform == "win32":
    from wexpect import run, spawn  # noqa: F401
