# PyOS
# Made for Python 2.7
# programs/cp.py

# Import Libraries
# PyOS Scripts
import internal.extra
import os
import shutil


def displayCwdFiles():
    """Get files and folders in current working directory and display them prettily."""
    file_list = os.listdir(os.getcwd())
    # Make a list of all files in current folder
    for Idx, file_name in enumerate(file_list):
        print("| {0} | {1} ".format(Idx, file_name))
    return file_list


def getFileOrigin(file_list):
    """Get input for file to be copied, and validate that it exists in the current folder (or filesystem)."""
    origin_file = raw_input("[0-" + str(len(file_list)) + "] > ")
    # Check to see if input was a valid number
    if origin_file.isdigit() and (int(origin_file) >= 0) and (int(origin_file) <= len(file_list) - 1):
            origin_file = file_list[int(origin_file)]
    # Default file to copy is first element of the list
    if origin_file == "":
        origin_file = file_list[0]
    return origin_file


from internal.baseapp import BaseApp
class App(BaseApp):
    usage_message = "cp [source] [dest]"
    required_args = 2

    def go(self, args):

        src = self.FileMgmt.getFullFilePath(args[1])
        dst = self.FileMgmt.getFullFilePath(args[2])

        # Validate chosen file to copy
        while not os.path.isfile(src):
            print(self.Colors.Warning("Warning! File " + args[1] + " does not exist!"))
            return
        
        if args[2] == "":
            dst = src + ".bak"
            args[2] = dst.split("\\")[1]
        
        print("Copying: " + args[1] + " to " + args[2])
        #print("Copying: " + src + " to " + dst)
        shutil.copy(src, dst)
        
