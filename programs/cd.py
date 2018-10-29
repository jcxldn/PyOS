# PyOS
# Made for Python 2.7
# programs/cd.py

# Import Libraries
# PyOS Scripts
import internal.extra
import internal.runCommand
# OS to use chdir
import os

def app(dir):
    try:
        os.chdir(dir)
        print "Changed dirs to %s" % dir
    except:
        print "Error changing dirs"
