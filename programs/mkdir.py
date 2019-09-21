import os

from internal.baseapp import BaseApp

class App(BaseApp):
    usage_message = "mkdir [dir] ..."
    required_args = 1

    def go(self, args):

        args.pop(0)

        for i in range(len(args)):
            path = os.path.join(self.FileMgmt.getFolderPath(), args[i])

            # If the path is taken, warn the user and skip this directory
            if os.path.exists(path):
                print(self.Colors.Warning("Path '" + args[i] + "' already exists!"))
                continue

            # Path is free, make the folder
            os.mkdir(os.path.join(self.FileMgmt.getFolderPath(), args[i]))
