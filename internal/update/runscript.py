# PyOS
# Made for Python 2.7
# internal/update/runscript.py

# See ghstatscustom.py for more infomation.

# Import custom file
import ghstatscustom
# PyOS Scripts
import internal.extra

def getfile():
	ghstatscustom.main("Prouser123", "PyOS", None, True, True)

# print("Getting version from text file")

def readfile():
	with open("latest.txt") as f:
		latest_version = f.read().split("\n")#[line_number]
		print(latest_version[1])
		ver = latest_version[1]
		ver = ver[1:]
		print("ver:: " + ver)

def app():
	print(internal.extra.colors.BOLD + "PyOS Update Checker" + internal.extra.colors.ENDC)
	print("Checking for updates...")
	getfile()
	with open("latest.txt") as f:
		latest_version = f.read().split("\n")#[line_number]
		print(latest_version[1])
		ver = latest_version[1]
		ver = ver[1:]
	print("The installed version is " + internal.extra.notes.ver + ". The most recent public release is " + ver + ". To update please visit: https://github.com/Prouser123/PyOS/releases/latest")

