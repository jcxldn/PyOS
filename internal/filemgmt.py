import os

class FileManagement:
    data_folder = "userdata"

    def open(self, filename, otype):
        self.createIfNotPresent()
        new_path = os.path.relpath('.\\' + self.data_folder + '\\' + filename, os.getcwd())
        return open(new_path, otype)

    def createIfNotPresent(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def getFullFilePath(self, filename):
        self.createIfNotPresent()
        return os.path.relpath('.\\' + self.data_folder + "\\" + filename, os.getcwd())

    def getFolderPath(self):
        self.createIfNotPresent()
        return os.path.relpath('.\\' + self.data_folder + "\\", os.getcwd())
