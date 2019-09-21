# PyOS
# Made for Python 2.7
# programs/sysinfo.py

# Import Libraries
import platform
import getpass
import socket
import os

# Import the base application class.
from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self):
        print(self.Colors.Bold("System Infomation"))
        # Print PyOS Version
        print(self.global_name + " " + self.global_ver)
        # Print System Version
        print("Python " + self.global_python_version)
        print("OS: " + platform.system() + ' ' + platform.release())
        print("OS Build: " + platform.version())
        print("Architecture: " + platform.machine())
        print("User: " + getpass.getuser())
        print("Hostname: " + socket.gethostname())
        print("Process ID: " + str(os.getpid()))
        print("Working Directory: " + os.getcwd())
        try:
            # This will fail on Windows, we will just ignore it.
            print("Home Directory: " + os.environ['HOME'])
        except Exception:
            return