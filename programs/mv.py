import os

from internal.baseapp import BaseApp

class App(BaseApp):
    usage_message = "mv [source] [dest]"
    required_args = 2

    def go(self, args):
        src = self.FileMgmt.getFullFilePath(args[1])
        dst = self.FileMgmt.getFullFilePath(args[2])

         # Validate chosen file to move
        while not os.path.isfile(src):
            print(self.Colors.Warning("File '" + args[1] + "' does not exist!"))
            return

        # Validate that there is not an already existing file on the destination
        while os.path.isfile(dst):
            if (len(args) is not 4):
                print(self.Colors.Warning("File '" + args[2] + "' already exists!\nPlease rename the file or add 'force' to force the move."))
                return
            elif args[3] == "force":
                print(self.Colors.Warning("You have used the force flag, which will overwrite existing files."))
                
                # Remove the destination file as we already check for duplicates.
                os.remove(dst)

                break

        if args[2] == "":
            dst = src + ".bak"
            args[2] = dst.split("\\")[1]

        print("Moving: '" + args[1] + "' to '" + args[2] + "'")

        # Rename / move the file
        os.rename(src, dst)