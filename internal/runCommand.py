# PyOS
# Made for Python 2.7.12
# internal/runCommand.py

# Import Libraries

import sys
from inspect import getmembers, isfunction
# PyOS Scripts
import extra

# Commands

class commands(object):
    @staticmethod
    def exit():
        print("Exiting...")
        sys.exit(0)
    
    @staticmethod
    def help():
        print("Commands: " + ', '.join([ x for x in dir(commands) if "_" not in x ]))

# Check if command is valid
def isValid(command):
    if command in dir(commands):
        print(extra.colors.OKBLUE + "Command is valid." + extra.colors.ENDC)
        
        # Run the command
        getattr(commands, command)()

    else:
        # Print an error
        print (extra.colors.FAIL + "Invalid command." + extra.colors.ENDC)