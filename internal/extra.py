# PyOS
# Made for Python 2.7
# internal/extra.py

# Import Libraries
import platform
import os

# OS Notes

class notes:
    name = ("PyOS")
    ver = ("3.1-base-master")
    author = ("Prouser123")
    helpmsg = ("Type 'help' for a list of commands.")

# System Info
class system:
    pyVer = (platform.python_version())

# Checks
class checks:
    # Check if float
    @staticmethod
    def isFloat(var):
        return isinstance(var, float)

# Commands

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
