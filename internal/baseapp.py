# PyOS
# Made for Python 2.7
# internal/baseapp.py

import internal.extra
import internal.runCommand
import internal.colors
import internal.filemgmt

class BaseApp:
    # Colors Class
    Colors = internal.colors.Colors()

    # FileManagement Class
    FileMgmt = internal.filemgmt.FileManagement()

    # Global variables
    global_name = internal.extra.notes.name
    global_ver = internal.extra.notes.ver
    global_author = internal.extra.notes.author
    global_python_version = internal.extra.system.pyVer

    # Program Specific Variables
    usage_message = "Message not found."
    required_args = 0

    def __init__(self, args):
        if (len(args) <= self.required_args):
            print("Usage: " + self.usage_message)
            return

        # The check passed, run the program code.
        self.go(args)

    def go(self, args):
        print("Hello, World!")
        print("There was no go function defined in your code. :(")

    def warn(self, msg):
        print(self.Colors.Warning(msg))

    def clear(self):
        internal.runCommand.BasicCommands.clear()
