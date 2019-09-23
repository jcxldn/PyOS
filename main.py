# PyOS
# Made for Python 2.7
# main.py

# Import Libraries

try:
  # readline for Linux / Darwin
  import readline
except ImportError:
  # pyreadline for Windows
  import pyreadline as readline
# PyOS Scripts
import internal.extra
import internal.runCommand

# Setup colors
import internal.colors
Colors = internal.colors.Colors()

# Command Auto Completer

def cmd_complete(text, state):
    for cmd in internal.runCommand.getValidCommands():
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
#print(internal.extra.colors.BOLD + internal.extra.notes.name + " " + internal.extra.notes.ver + " - " + internal.extra.colors.WARNING + "Made for Python 2.7" + internal.extra.colors.ENDC)
print(Colors.Bold(internal.extra.notes.name + " " + internal.extra.notes.ver + " - ") + Colors.Warning("Made for Python 2.7"))
# Print python version
print("Running on Python " + internal.extra.system.pyVer)
print(str(len(internal.runCommand.getValidCommands())) + " programs detected.")
print(internal.extra.notes.helpmsg)
cmd_loop()
