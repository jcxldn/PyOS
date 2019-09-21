import requests

from internal.baseapp import BaseApp

class App(BaseApp):
    usage_message = "downloader [url] <filename>"
    required_args = 1

    def go(self, args):
        self.clear()
        print(self.Colors.Bold("Downloader"))

        url = args[1]

        file_name = url.split("/")
        file_name_index = len(file_name) - 1
        file_name = file_name[file_name_index]
        print "Downloading..."
        try:
            r = requests.get(url)

            # Display some information about the request
            print("Got code {0} in {1} seconds".format(r.status_code,  r.elapsed.total_seconds()))

            # If the user provided a filename, then we will save under that name.
            if (len(args) >= 3 and args[2] != ""):
                file_name = args[2]

            with self.FileMgmt.open(file_name, "wb") as f:
                f.write(r.content)
            print "File saved as %s" % file_name
        except Exception as e:
            self.warn(str(e))
