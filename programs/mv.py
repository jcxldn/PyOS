# PyOS
# Made for Python 2.7
# programs/mv.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os

def app():
    print(internal.extra.colors.OKGREEN + "Moving (renaming) files: " + internal.extra.colors.ENDC)
    print(internal.extra.colors.BOLD + "File to move/rename (enter filename or number of file): " + internal.extra.colors.ENDC)
    file_list = os.listdir(os.getcwd())
    # Make a list of all files in current folder
    for Idx, file_name in enumerate(file_list):
        print("| {0} | {1} ".format(Idx, file_name))
    def getfileOrigin():
        """Get input for file to be copied, and validate that it exists in the current folder (or filesystem)."""
        origin_file = raw_input("[0-" + str(len(file_list)) + "] > ")
        # Check to see if input was a valid number
        if origin_file.isdigit() and (int(origin_file) >= 0) and (int(origin_file) <= len(file_list) - 1):
                origin_file = file_list[int(origin_file)]
        # Default file to copy is first element of the list
        if origin_file == "":
            origin_file = file_list[0]
        return origin_file
    origin_file = getfileOrigin()
    # Validate chosen file to move
    while not os.path.isfile(origin_file):
        print(internal.extra.colors.BOLD + "Warning! file " + origin_file + " does not yet exist.\n\n"  + internal.extra.colors.ENDC)
        origin_file = getfileOrigin()
    print(internal.extra.colors.BOLD + origin_file + " selected for moving." + internal.extra.colors.ENDC)
    target_file = raw_input(internal.extra.colors.BOLD + "Enter filename to move to [Enter to backup]:"  + internal.extra.colors.ENDC)
    if target_file == "":
        target_file = origin_file + ".bak"
    if os.path.isfile(target_file):
        target_file = raw_input(internal.extra.colors.BOLD + "Warning! File " + target_file + "exists.\n\
                                Overwrite [y/0/Enter] or back-up [b/1]?"  + internal.extra.colors.ENDC)
        if target_file.lower() == '' or target_file.lower() == 'y' or target_file == '0':
            target_file = target_file
        elif target_file.lower() == '' or target_file.lower() == 'y' or target_file == '1':
            target_file += '.1'
        else:
            target_file = os.devnull()
    print("Target file: " + target_file + " selected.")
    os.rename(origin_file, target_file)

