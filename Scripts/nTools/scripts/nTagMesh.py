# python
import re

import lx
import modo
import modo.dialogs

arg = lx.arg()
assert isinstance(arg, str)
scene = modo.Scene()


# position: 0 = prefix, 1 = suffix
def set_tag(text, position):
	try:
		selected_items = scene.selectedByType("mesh")
	except IndexError:
		modo.dialogs.alert("Error", "Wrong selection.\nNo item selected in the item list.")
		return

	for item in selected_items:
		if re.search(text, item.name):
			return

		if position == 1:
			item.name = item.name + text
		elif position == 0:
			item.name = text + item.name


if arg[0] == "_" and arg[len(arg) - 1] == "_":
	modo.dialogs.alert("Error", "Wrong argument.\n%s" % arg)
elif arg[0] == "_":
	set_tag(arg, 1)
elif arg[len(arg) - 1] == "_":
	set_tag(arg, 0)
