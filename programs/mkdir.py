# PyOS
# Made for Python 2.7
# programs/mkdir.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os

def app():
    """"""
    print(internal.extra.colors.OKGREEN + "Creating directories: " + internal.extra.colors.ENDC)
    dir_list = raw_input(internal.extra.colors.BOLD + "Enter list of directories, separated by commas: " + internal.extra.colors.ENDC)
    dir_list = dir_list.split(',')
    os.makedirs(os.path.join(os.getcwd(), *dir_list))
