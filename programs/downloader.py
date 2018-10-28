# PyOS
# Made for Python 2.7
# programs/downloader.py

# Import Libraries
# PyOS Scripts
import internal.extra
import internal.runCommand
# Requests library
import requests

def app():
    internal.runCommand.commands.clear()
    print internal.extra.colors.BOLD + "Downloader" + internal.extra.colors.ENDC

    url = raw_input("Enter file url: ")
    file_name = url.split("/")[len(url.split("/")) - 1]
    print "Downloading..."
    try:
        r = requests.get(url)
        with open(file_name, "wb") as f:
            f.write(r.content)
        print "File saved as %s" % file_name
    except Exception as e:
        print "An error occured"
        if input("Show error message (y/n): ") in ["y", "Y"]:
            print e
