# PyOS
# Made for Python 2.7
# internal/extra.py

# Import Libraries
import platform
import os

# OS Notes

class notes:
    name = ("PyOS")
    ver = ("2.2-base-master")
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

# Commands

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
