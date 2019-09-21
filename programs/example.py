# PyOS
# Made for Python 2.7
# programs/example.py


# Import the base application class.
from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self, args):
        # This is the function that will run when the 'example' command is typed in.

        # Clear the console screen
        self.clear()

        """
        This line of code print "PyOS Example Program" in Bold.
        You can use self.Colors to use other text styles and colors.
        """
        print(self.Colors.Bold("PyOS Example Program"))

        # Print sample text
        print("Hello, World!")
