# PyOS
# Made for Python 2.7.12
# internal/extra.py

# Import Libraries
import platform

# OS Notes

class os:
    name = ("PyOS")
    ver = ("DEV")
    author = ("Prouser123")
    helpmsg = ("Type 'help' for a list of commands.")

# System Info
class system:
    pyVer = (platform.python_version())

# Text Color

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Checks

class checks:
    # Check if float
    @staticmethod
    def isFloat(var):
        return isinstance(var, float)