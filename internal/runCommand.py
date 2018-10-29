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
        # Run built-in function
        internal.extra.cls()

    @staticmethod
    def cls():
        # Run built-in function
        return commands.clear()

    @staticmethod
    def about():
        # Run code below (no function necessary)
        print(internal.extra.colors.BOLD + internal.extra.notes.name + " " + internal.extra.notes.ver + internal.extra.colors.ENDC)
        print("Author: " + internal.extra.notes.author)
        print("For more infomation please read the README.md and DOCUMENTATION.md files in the project folder.")

    @staticmethod
    def calc():
        # Run external file
        programs.calculator.app()

    @staticmethod
    def sysinfo():
        # Run external file
        programs.sysinfo.app()

    @staticmethod
    def updater():
        # Run updater file
        internal.update.runscript.app()

    @staticmethod
    def example():
        # Run external file
        programs.example.app()

    @staticmethod
    def fizzbuzz():
        # Run external file
        programs.fizzbuzz.app()

    @staticmethod
    def ls():
        # Run external file
        programs.ls.app()

    @staticmethod
    def pwd():
        # Run external file
        programs.pwd.app()

    @staticmethod
    def snake_game():
        # Starts Snake Game
        programs.snake_game.app()

# Check if command is valid
def isValid(command):
    if command in [ x for x in dir(commands) if "_" not in x ]:
        # print(extra.colors.OKBLUE + "Command is valid." + extra.colors.ENDC)

        # Run the command
        getattr(commands, command)()

    else:
        # Print an error
        print (internal.extra.colors.FAIL + "Invalid command. " + internal.extra.notes.helpmsg + internal.extra.colors.ENDC)
