# python

# NOTES:
# -	That script isn't magical, the symmetry will only work if the mesh is symmetrical
#   on the axis you chose.
# -	Best used with a macro. Take a look at nSymmetryX.lxm for an example.

import lx
import lxu.select
import modo
import modo.dialogs


def calculate():
	scene = modo.Scene()
	axis = lx.eval("symmetry.axis ?")
	chan_eval = scene.Channels(None, 0.0)
	items = lxu.select.ItemSelection()

	if len(items.current()) > 1:
		modo.dialogs.alert("Error", "Multiple items selected.\nPlease select a single item.")
		return

	surface_item = lx.object.SurfaceItem(items.current()[0])
	surface = surface_item.GetSurface(chan_eval, 0)
	assert isinstance(surface, lx.object.Surface)
	bbox = surface.GetBBox()
	offset = (bbox[0][axis] + bbox[1][axis]) / 2
	lx.eval("select.symmetry true offset:%s" % offset)


calculate()
