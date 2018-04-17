# PyOS
# Made for Python 2.7.12
# internal/sysinfo.py

# Import Libraries

# PyOS Scripts
import extra

def start():
    print(extra.colors.BOLD + "System Infomation" + extra.colors.ENDC)
    # Print PyOS Version
    print(extra.os.name + " " + extra.os.ver  + extra.colors.ENDC)
    # Print System Version
    print("Python " + extra.system.pyVer)