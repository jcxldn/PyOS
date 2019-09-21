# PyOS
# Made for Python 2.7
# programs/example.py

# Import the internal.extra script and give it the shortcut of 'e'.
import internal.extra as e


# Import the base application class.
from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self):
        # This is the function that will run when the 'example' command is typed in.

        # Clear the console screen
        e.cls()

        """
        This line of code below the BOLD text style, prints some text and resets the text style.
        You can use the internal.extra.colors class to use text styles.

        In this script internal.extra has been set to 'e',
        so e.colors will work to access color styles.
        """
        print(e.colors.BOLD + "PyOS Example Program" + e.colors.ENDC)

        # Print sample text
        print("Hello, World!")
