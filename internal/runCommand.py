# PyOS
# Made for Python 2.7
# internal/runCommand.py

# Import Libraries

import sys
# PyOS Scripts
import internal.extra
import internal.update.runscript
# External Programs
import programs.calculator
import programs.sysinfo
import programs.example
import programs.fizzbuzz
import programs.ls
import programs.pwd
import programs.cp
import programs.mv
import programs.mkdir
import programs.downloader
import programs.snake
import programs.showallcolors
import programs.help

def getValidCommands():
    return [ x for x in dir(programs) if "_" not in x ] + getBasicCommands()

def getBasicCommands():
    return [ x for x in dir(BasicCommands) if "_" not in x ]

# Basic Commands

class BasicCommands(object):
    @staticmethod
    def exit():
        print("Exiting...")
        BasicCommands.clear()
        sys.exit(0)

    @staticmethod
    def help():
        # Print all functions that do not include an underscore
        print("Commands: " + ', '.join(getValidCommands()))

    @staticmethod
    def clear():
        # Run built-in function
        internal.extra.cls()

    @staticmethod
    def cls():
        # Run built-in function
        return BasicCommands.clear()

    @staticmethod
    def about():
        # Run code below (no function necessary)
        print(internal.extra.colors.BOLD + internal.extra.notes.name + " " + internal.extra.notes.ver + internal.extra.colors.ENDC)
        print("Author: " + internal.extra.notes.author)
        print("For more infomation please read the README.md and DOCUMENTATION.md files in the project folder.")


# Check if command is valid
def isValid(command):
    args = command.split(" ")
    if args[0] in getValidCommands():
        # Run the command

        # Check if the item is a basic command
        if args[0] in getBasicCommands():
            getattr(BasicCommands, args[0])()
        else:
            # Item is in it's own file.
            getattr(programs, args[0]).App(args)

    else:
        # Print an error
        print (internal.extra.colors.FAIL + "Invalid command. " + internal.extra.notes.helpmsg + internal.extra.colors.ENDC)
