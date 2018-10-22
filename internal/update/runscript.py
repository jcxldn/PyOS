# PyOS
# Made for Python 2.7
# internal/update/runscript.py

# See ghstatscustom.py for more infomation.

# Import custom file
import internal.update.ghstatscustom as ghstatscustom
# PyOS Scripts
import internal.extra

def getfile():
	ghstatscustom.main("Prouser123", "PyOS", None, True, True)

# print("Getting version from text file")

def app():
	print(internal.extra.colors.BOLD + "PyOS Update Checker" + internal.extra.colors.OKBLUE)
	print("Checking for updates...")
	getfile()
	with open("latest.txt") as f:
		print(internal.extra.colors.ENDC)
		latest_version = f.read().split("\n")#[line_number]
		#print(latest_version[1])
		ver = latest_version[1]
		ver = ver[1:]
	print("Installed Version: " + internal.extra.colors.WARNING + internal.extra.notes.ver + internal.extra.colors.ENDC)
	print("Newest Version: " + internal.extra.colors.WARNING + ver + internal.extra.colors.ENDC)
	try:
		if (float(internal.extra.notes.ver) >= float(ver)):
			print("You are up-to-date!")
		else:
			print("There is a new version available.")
			print("To update please visit: https://github.com/Prouser123/PyOS/releases/latest")
	except Exception as e:
		print("Unable to verify if you are up-to-date.")
		print("To update please visit: https://github.com/Prouser123/PyOS/releases/latest")
