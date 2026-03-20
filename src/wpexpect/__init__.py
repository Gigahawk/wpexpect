import sys


if sys.platform == "win32":
    from wexpect import run, spawn  # noqa: F401
    import pexpect

    globals().update(
        {
            name: getattr(pexpect, name)
            for name in dir(pexpect)
            if not name.startswith("_")
            and name not in ("spawn", "run", "spawnu", "runu")
        }
    )
else:
    from pexpect import *
