"""Entry point. Checks for user and starts main script"""

# ÂŠī¸ Dan Gazizullin, 2021-2022
# This file is a part of Hikka Userbot
# đ https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# đ https://www.gnu.org/licenses/agpl-3.0.html

import getpass
import os
import subprocess
import sys

from ._internal import restart

if (
    getpass.getuser() == "root"
    and "--root" not in " ".join(sys.argv)
    and all(trigger not in os.environ for trigger in {"DOCKER", "GOORM"})
):
    print("đĢ" * 15)
    print("You attempted to run Hikka on behalf of root user")
    print("Please, create a new user and restart script")
    print("If this action was intentional, pass --root argument instead")
    print("đĢ" * 15)
    print()
    print("Type force_insecure to ignore this warning")
    if input("> ").lower() != "force_insecure":
        sys.exit(1)


if sys.version_info < (3, 8, 0):
    print("đĢ Error: you must use at least Python version 3.8.0")
elif __package__ != "hikka":  # In case they did python __main__.py
    print("đĢ Error: you cannot run this as a script; you must execute as a package")
else:
    try:
        # If telethon is not installed, just skip to a part of main startup
        # then main.py will through an error and re-install all deps
        import telethon
    except Exception:
        pass
    else:
        try:
            import telethon

            if tuple(map(int, telethon.__version__.split("."))) < (1, 24, 12):
                raise ImportError
        except ImportError:
            print("đ Installing Hikka-TL...")

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--force-reinstall",
                    "-q",
                    "--disable-pip-version-check",
                    "--no-warn-script-location",
                    "hikka-tl",
                ],
                check=True,
            )

            restart()

        try:
            import pyrogram

            if tuple(map(int, pyrogram.__version__.split("."))) < (2, 0, 61):
                raise ImportError
        except ImportError:
            print("đ Installing Hikka-Pyro...")

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--force-reinstall",
                    "-q",
                    "--disable-pip-version-check",
                    "--no-warn-script-location",
                    "hikka-pyro",
                ],
                check=True,
            )

            restart()

    try:
        from . import log

        log.init()

        from . import main
    except (ModuleNotFoundError, ImportError) as e:
        print(f"{str(e)}\nđ Attempting dependencies installation... Just wait âą")

        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "-q",
                "--disable-pip-version-check",
                "--no-warn-script-location",
                "-r",
                "requirements.txt",
            ],
            check=True,
        )

        restart()

    if __name__ == "__main__":
        if "HIKKA_DO_NOT_RESTART" in os.environ:
            del os.environ["HIKKA_DO_NOT_RESTART"]

        main.hikka.main()  # Execute main function
