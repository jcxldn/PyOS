# PyOS
# Made for Python 2.7
# internal/sysinfo.py

# Import Libraries
import platform
import getpass
import socket
import os
# PyOS Scripts
import internal.extra

def start():
    print(internal.extra.colors.BOLD + "System Infomation" + internal.extra.colors.ENDC)
    # Print PyOS Version
    print(internal.extra.notes.name + " " + internal.extra.notes.ver  + internal.extra.colors.ENDC)
    # Print System Version
    print("Python " + internal.extra.system.pyVer)
    print("OS: " + platform.system() + ' ' + platform.release())
    print("OS Build: " + platform.version())
    print("Architecture: " + platform.machine())
    print("User: " + getpass.getuser())
    print("Hostname: " + socket.gethostname())
    print("Process ID: " + str(os.getpid()))
    print("Working Directory: " + os.getcwd())
    try:
        # This will fail on Windows, we will just ignore it.
        print("Home Directory: " + os.environ['HOME'])
    except Exception:
        return