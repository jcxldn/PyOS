# PyOS
# Made for Python 2.7
# internal/runCommand.py

# Import Libraries

import sys
# PyOS Scripts
import internal.extra
import internal.calculator
import internal.sysinfo

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
        extra.cls()

    @staticmethod
    def cls():
        return commands.clear()

    @staticmethod
    def about():
        print(extra.notes.name + " " + extra.notes.ver)
        print("Author: " + extra.notes.author)

    @staticmethod
    def calc():
        calculator.start()

    @staticmethod
    def sysinfo():
        sysinfo.start()

# Check if command is valid
def isValid(command):
    if command in [ x for x in dir(commands) if "_" not in x ]:
        # print(extra.colors.OKBLUE + "Command is valid." + extra.colors.ENDC)

        # Run the command
        getattr(commands, command)()

    else:
        # Print an error
        print (extra.colors.FAIL + "Invalid command. " + extra.notes.helpmsg + extra.colors.ENDC)