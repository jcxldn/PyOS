# PyOS
# Made for Python 2.7
# main.py

# Import Libraries

try:
  import readline
except ImportError:
  import pyreadline as readline
# PyOS Scripts
import internal.extra
import internal.runCommand

# Command Auto Completer

def cmd_complete(text, state):
    for cmd in [ x for x in dir(internal.runCommand.commands) if "_" not in x ]:
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
    internal.runCommand.isValid(command)
    cmd_loop()

# Initial Code

# Clear the screen
internal.extra.cls()
# Print the name and version
print(internal.extra.colors.BOLD + internal.extra.notes.name + " " + internal.extra.notes.ver + " - " + internal.extra.colors.WARNING + "Made for Python 2.7" + internal.extra.colors.ENDC)
# Print python version
print ("Running on Python " + internal.extra.system.pyVer)
print(internal.extra.notes.helpmsg)
cmd_loop()