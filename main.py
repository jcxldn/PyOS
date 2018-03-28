# PyOS
# Made for Python 2.7.12
# main.py

# Import Libraries

import os
# PythonOS Scripts
from internal import extra

# Define Variables

os_name = ("PyOS")
os_ver = ("DEV")

# Command Loop

def cmd_loop():
    command = raw_input("> ")
    
# Initial Code

# Clear the screen
os.system('clear')
# Print the name and version
print(os_name + " " + os_ver)

print(extra.colors.WARNING + extra.colors.BOLD + "Note: PyOS was designed for Python v2, not v3." + extra.colors.ENDC)
cmd_loop()