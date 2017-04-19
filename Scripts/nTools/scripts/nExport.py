# python

import os
import re
import sys
import lx
import modo
import modo.dialogs

arg = lx.arg()
scene = modo.Scene()
scene_name = scene.name
assert isinstance(scene_name, str)
scene_name = os.path.splitext(scene_name)[0]
old_selection = scene.selected


def export_path():
	scene_path = scene.filename
	try:
		assert isinstance(scene_path, str)
	except AssertionError:
		modo.dialogs.alert("Error", "Save the scene before exporting.")
		sys.exit()

	scene_path = os.path.split(scene_path)[0]
	path = os.path.join(scene_path, "%s_Geometry" % scene_name)
	if not os.path.exists(path):
		os.makedirs(path)
	return path


def mesh_path(mesh_name):
	path = export_path()
	path = os.path.join(path, "%s.fbx" % mesh_name)
	return path


def export_selection():
	try:
		selected_items = scene.selectedByType("mesh")
	except IndexError:
		modo.dialogs.alert("Error", "Wrong selection.\nNo item selected in the item list.")
		return

	# Cleanup selected_items
	for item in selected_items:
		if item.parents:
			# Don't want to export a child
			selected_items.remove(item)
			# If the parent is already selected, remove it to avoid duplicates
			try:
				selected_items.remove(item.parents[-1])
			except ValueError:
				pass
			# Append parent to selected_item
			selected_items.append(item.parents[-1])
		if re.search("dntxprt", item.name):
			selected_items.remove(item)

	# Actual export
	for item in selected_items:
		assert isinstance(item, modo.Mesh)
		scene.select(item)
		lx.eval('scene.saveAs "%s" fbx true' % mesh_path(item.name))


def restore_state():
	scene.select(old_selection)


def select_all():
	meshes_to_export = scene.meshes
	for mesh in meshes_to_export:
		if mesh.parents:
			meshes_to_export.remove(mesh)
	scene.select(meshes_to_export)


if arg == "selection":
	export_selection()
	restore_state()

if arg == "all":
	select_all()
	export_selection()
	restore_state()
