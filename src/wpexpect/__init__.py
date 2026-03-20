import sys

from pexpect import *

if sys.platform == "win32":
    from wexpect import run, spawn
