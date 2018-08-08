# PyOS
# Made for Python 2.7
# internal/sysinfo.py

# Import Libraries
import sys
import platform
import getpass
import socket
import os
# PyOS Scripts
import extra

def start():
    print(extra.colors.BOLD + "System Infomation" + extra.colors.ENDC)
    # Print PyOS Version
    print(extra.notes.name + " " + extra.notes.ver  + extra.colors.ENDC)
    # Print System Version
    print("Python " + extra.system.pyVer)
    print("OS: " + sys.platform)
    print("Architecture: " + platform.machine())
    print("User: " + getpass.getuser())
    print("Hostname: " + socket.gethostname())
    try:
        # This will fail on Windows, we will just ignore it.
        print("Home Directory: " + os.environ['HOME'])
    except Exception:
        pass