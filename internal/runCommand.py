# PyOS
# Made for Python 2.7.12
# internal/runCommand.py

# Import Libraries

import sys
import os
from inspect import getmembers, isfunction
# PyOS Scripts
import extra

# Commands

class commands(object):
    @staticmethod
    def exit():
        print("Exiting...")
        commands.clear()
        sys.exit(0)
    
    @staticmethod
    def help():
        # Print all functions that do not include an underscore
        print("Commands: " + ', '.join([ x for x in dir(commands) if "_" not in x ]))
    
    @staticmethod
    def clear():
        os.system('clear')
    
    @staticmethod
    def cls():
        return commands.clear()
    
    @staticmethod
    def about():
        print(extra.os.name + " " + extra.os.ver)
        print("Author: " + extra.os.author)

# Check if command is valid
def isValid(command):
    if command in dir(commands):
        # print(extra.colors.OKBLUE + "Command is valid." + extra.colors.ENDC)
        
        # Run the command
        getattr(commands, command)()

    else:
        # Print an error
        print (extra.colors.FAIL + "Invalid command." + extra.colors.ENDC)