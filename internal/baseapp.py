# PyOS
# Made for Python 2.7
# internal/baseapp.py

import internal.extra

class BaseApp:
    usage_message = "Message not found."
    required_args = 0

    def __init__(self, args):
        if (len(args) <= self.required_args):
            print("Usage: " + self.usage_message)
            return
        
        # The check passed, run the program code.
        try:
            self.go(args)
        except TypeError:
            self.go()
    
    def go(self):
        print("Hello, World!")
        print("There was no go function defined in your code. :(")

    def go(self, args):
        self.go()

    def warn(self, message):
        print(internal.extra.colors.WARNING + message + internal.extra.colors.ENDC)