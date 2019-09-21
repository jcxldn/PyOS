# PyOS
# Made for Python 2.7
# internal/programs/showallcolors.py

import sys

# Import the base application class.
from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self, args):
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
            print u"\u001b[0m"