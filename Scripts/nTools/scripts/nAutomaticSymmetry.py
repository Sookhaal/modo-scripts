# python
from lib2to3.fixer_util import is_import

import lx
import modo
import modo.dialogs


def calculate():
	scene = modo.Scene()
	try:
		selected_item = scene.selectedByType("mesh")[0]
	except IndexError:
		modo.dialogs.alert("Error", "Wrong selection.\nNo item selected in the item list.")
		return

	assert isinstance(selected_item, modo.Mesh)
	selected_polygons = list(selected_item.geometry.polygons.selected)

	if not 0 != len(selected_polygons) <= 1:
		modo.dialogs.alert("Error", "Wrong selection.\nPlease select a single polygon.")
		return

	polygon = selected_polygons[0]
	assert isinstance(polygon, modo.MeshPolygon)

	# Get the index of the highest & lowest normal value
	# if normal = (-1, 0.5, -0.2)
	# max_normal_index = 1 because normal[1] is the highest value
	# min_normal_index = 0 because normal[0] is the lowest value
	max_normal_index = polygon.normal.index(max(polygon.normal))
	min_normal_index = polygon.normal.index(min(polygon.normal))

	# Choose the symmetry axis (0 = X, 1 = Y, 2 = Z)
	if abs(polygon.normal[max_normal_index]) > abs(polygon.normal[min_normal_index]):
		symmetry_axis = max_normal_index
	elif abs(polygon.normal[max_normal_index]) < abs(polygon.normal[min_normal_index]):
		symmetry_axis = min_normal_index
	else:
		modo.dialogs.alert("Error", "Can't find a good axis.\nPlease select another polygon.")
		return

	# Activate the symmetry
	lx.eval("symmetry.state true")
	lx.eval("symmetry.axis %s" % symmetry_axis)
	lx.eval("@nUpdateSymmetryOffset.py")


calculate()