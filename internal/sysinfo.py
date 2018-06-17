# PyOS
# Made for Python 2.7
# internal/sysinfo.py

# Import Libraries
import sys
# PyOS Scripts
import extra

def start():
    print(extra.colors.BOLD + "System Infomation" + extra.colors.ENDC)
    # Print PyOS Version
    print(extra.notes.name + " " + extra.notes.ver  + extra.colors.ENDC)
    # Print System Version
    print("Python " + extra.system.pyVer)
    print("OS: " + sys.platform)