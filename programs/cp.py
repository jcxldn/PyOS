import os
import shutil

from internal.baseapp import BaseApp

class App(BaseApp):
    usage_message = "cp [source] [dest]"
    required_args = 2

    def go(self, args):
        src = self.FileMgmt.getFullFilePath(args[1])
        dst = self.FileMgmt.getFullFilePath(args[2])

        # Validate chosen file to copy
        while not os.path.isfile(src):
            print(self.Colors.Warning("File '" + args[1] + "' does not exist!"))
            return

        if args[2] == "":
            dst = src + ".bak"
            args[2] = dst.split("\\")[1]

        print("Copying: '" + args[1] + "' to '" + args[2] + "'")
        #print("Copying: " + src + " to " + dst)
        shutil.copy(src, dst)
