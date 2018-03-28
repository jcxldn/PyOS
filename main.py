# PyOS
# Made for Python 2.7.12
# main.py

# Import Libraries

import os
# PyOS Scripts
from internal import extra
from internal import runCommand

# Define Variables

os_name = ("PyOS")
os_ver = ("DEV")

# Command Loop

def cmd_loop():
    command = raw_input("> ")
    runCommand.isValid(command)
    cmd_loop()
    
# Initial Code

# Clear the screen
os.system('clear')
# Print the name and version
print(os_name + " " + os_ver)

print(extra.colors.WARNING + extra.colors.BOLD + "Note: PyOS was designed for Python v2, not v3." + extra.colors.ENDC)
cmd_loop()