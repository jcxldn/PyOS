# PyOS
# Made for Python 2.7.12
# internal/runCommand.py

# Import Libraries
import sys
import extra # PyOS Script

# Commands
class commands(object):
    @staticmethod
    def exit():
        print("Exiting...")
        sys.exit(0)
    
    @staticmethod
    def help():
        print("Commands: " + ', '.join(extra.commands))

# Check if command is valid
def isValid(command):
    if command in dir(commands):
        id = (extra.commands.index(command))
        print(extra.colors.OKBLUE + "Command is valid. ID: " + str(id) + extra.colors.ENDC)
        
        # Run the command
        getattr(commands, command)()

    else:
        # Print an error
        print (extra.colors.FAIL + "Invalid command." + extra.colors.ENDC)