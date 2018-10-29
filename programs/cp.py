# PyOS
# Made for Python 2.7
# programs/cp.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os
import shutil

def app():
    print(internal.extra.colors.OKGREEN + "Copying files: " + internal.extra.colors.ENDC)
    print(internal.extra.colors.BOLD + "File to copy from (enter filename or number of file): " + internal.extra.colors.ENDC)
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
    # Validate chosen file to copy
    while not os.path.isfile(origin_file):
        print(internal.extra.colors.BOLD + "Warning! file " + origin_file + " does not yet exist.\n\n"  + internal.extra.colors.ENDC)
        origin_file = getfileOrigin()
    print(internal.extra.colors.BOLD + origin_file + " selected for copying." + internal.extra.colors.ENDC)
    target_file = raw_input(internal.extra.colors.BOLD + "Enter filename to copy to [Enter to backup]:"  + internal.extra.colors.ENDC)
    if target_file == "":
        target_file = origin_file + ".bak"
    print("Target file: " + target_file + " selected.")
    shutil.copy(origin_file, target_file)
