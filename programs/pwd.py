# PyOS
# Made for Python 2.7
# programs/pwd.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os

def app():
    print(internal.extra.colors.OKGREEN + "Current working directory:" + internal.extra.colors.ENDC)
    print(os.getcwd())
