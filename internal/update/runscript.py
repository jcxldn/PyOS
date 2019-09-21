from distutils.version import LooseVersion

import internal.update.ghstatscustom as ghstatscustom

# Setup colors
import internal.colors
Colors = internal.colors.Colors()

def getfile():
	ghstatscustom.main("Prouser123", "PyOS", None, True, True)

def app():
	print(Colors.Bold("PyOS Update Checker"))
	print('\033[94m' + "Checking for updates...")
	getfile()
	print('\033[0m')
	with open("latest.txt") as f:
		latest_version = f.read().split("\n")#[line_number]
		#print(latest_version[1])
		ver = latest_version[1]
		ver = ver[1:]
	print("Installed Version: " + Colors.Warning(internal.extra.notes.ver))
	print("Newest Version: " + Colors.Warning(ver))
	try:
		if LooseVersion(internal.extra.notes.ver) >= LooseVersion(ver):
			print("You are up-to-date!")
		else:
			print("There is a new version available.")
			print("To update please visit: https://github.com/Prouser123/PyOS/releases/latest")
	except Exception:
		print("Unable to verify if you are up-to-date.")
		print("To update please visit: https://github.com/Prouser123/PyOS/releases/latest")
