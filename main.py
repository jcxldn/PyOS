# PyOS
# Made for Python 2.7
# main.py

# Import Libraries

try:
  import readline
except ImportError:
  import pyreadline as readline
# PyOS Scripts
from internal import extra
from internal import runCommand

# Command Auto Completer

def cmd_complete(text, state):
    for cmd in [ x for x in dir(runCommand.commands) if "_" not in x ]:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

# Command Loop

def cmd_loop():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(cmd_complete)
    command = raw_input("> ").lower()
    runCommand.isValid(command)
    cmd_loop()

# Initial Code

# Clear the screen
extra.cls()
# Print the name and version
print(extra.colors.BOLD + extra.notes.name + " " + extra.notes.ver + " - " + extra.colors.WARNING + "Made for Python 2.7" + extra.colors.ENDC)
# Print python version
print ("Running on Python " + extra.system.pyVer)
print(extra.notes.helpmsg)
cmd_loop()