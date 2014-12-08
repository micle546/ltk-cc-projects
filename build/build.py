from optparse import OptionParser
import sys
import os
import os.path
import re
import shutil
from distutils.dir_util import copy_tree

# program options
parser = OptionParser()

parser.add_option ("-p", "--project", action="store", type="str",
    dest="projectPath", default=None,
    help="Set the project path.")

(options, targets) = parser.parse_args()

#print options
#print targets

if options.projectPath is None:
    print ("We need a project path!")
    os.exit()

sourceName = "computercraft-remote-excavator-builder"
sourceDirs = [ "reb" ]

print("Curr dir = " + os.getcwd())
print("Project path = " + options.projectPath)

print ("Replicating files.")

items = os.listdir (options.projectPath)

for item in items:
	itemqf = str.lower (os.path.abspath (options.projectPath + os.sep + item))

	isNumber = re.search ("(\d+)", item) is not None

	if isNumber:
		for sourceDir in sourceDirs:
			sourcePath = options.projectPath + os.sep + sourceName + os.sep + sourceDir
			destPath = itemqf + os.sep + sourceDir

			print ("source={}, dest={}".format (sourcePath, destPath))

			copy_tree (sourcePath, destPath)
