# PyOS
# Made for Python 2.7
# internal/programs/showallcolors.py

import internal.extra

import sys

def app():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print u"\u001b[0m"