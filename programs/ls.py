import os

from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self, args):
        print(" | ".join(os.listdir(self.FileMgmt.getFolderPath())))