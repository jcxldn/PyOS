# PyOS
# Made for Python 2.7
# programs/ls.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os

def app():
    print(internal.extra.colors.OKGREEN + "Listing contents of your current directory:" + internal.extra.colors.ENDC)
    print(" | ".join(os.listdir(os.getcwd())))
