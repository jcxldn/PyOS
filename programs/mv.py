# PyOS
# Made for Python 2.7
# programs/mv.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os
from programs.cp import displayCwdFiles, getFileOrigin


def app():
    print(internal.extra.colors.OKGREEN + "Moving (renaming) files: " + internal.extra.colors.ENDC)
    print(internal.extra.colors.BOLD + "File to move/rename (enter filename or number of file): " + internal.extra.colors.ENDC)
    file_list = displayCwdFiles()
    origin_file = getFileOrigin(file_list)
    # Validate chosen file to move
    while not os.path.isfile(origin_file):
        print(internal.extra.colors.BOLD + "Warning! file " + origin_file + " does not yet exist.\n\n" + internal.extra.colors.ENDC)
        origin_file = getFileOrigin(file_list)
    print(internal.extra.colors.BOLD + origin_file + " selected for moving." + internal.extra.colors.ENDC)
    target_file = raw_input(internal.extra.colors.BOLD + "Enter filename to move to [Enter to backup]:" + internal.extra.colors.ENDC)
    if target_file == "":
        target_file = origin_file + ".bak"
    if os.path.isfile(target_file):
        existing_check = raw_input(
            internal.extra.colors.BOLD +
            "Warning! File " + target_file +
            " exists.\nOverwrite [y/0/Enter] or back-up [b/1]?" +
            internal.extra.colors.ENDC)
        if existing_check.lower() == 'b' or existing_check == '1':
            target_file += '.bak'
        elif existing_check != '' or existing_check.lower() != 'y' or existing_check != '0':
            target_file = origin_file
    print("Target file: " + target_file + " selected.")
    os.rename(origin_file, target_file)
