# PyOS
# Made for Python 2.7
# programs/pwd.py

# Import Libraries
import os

# Import the base application class.
from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self):
        print(self.Colors.Green("Current working directory: ") + self.Colors.Blue(os.getcwd()))
