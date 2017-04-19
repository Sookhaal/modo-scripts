# python

import sys
import subprocess
import modo
import lx

args = lx.args()
scene = modo.Scene()


def browse_to_scene():
	if scene.filename:
		if sys.platform == "win32":
			subprocess.Popen(r'explorer /select, "%s"' % scene.filename)


def browse_to_project():
	if scene.filename:
		if sys.platform == "win32":
			subprocess.Popen(r'explorer /select, "%s"' % scene.filename)


if args[0] == "BrowseToScene":
	browse_to_scene()

if args[0] == "BrowseToProject":
	browse_to_project()
