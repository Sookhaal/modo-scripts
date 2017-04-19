# Notes
* Some things might be broken (unfinished/missing scripts).

# Keybinds
I use [X-Mouse Button Control](https://www.highrez.co.uk/downloads/xmousebuttoncontrol.htm) to bind the mouse wheel to some keys.
![xMouse Layers](/Readme/Images/xmouse_1.png?raw=true)
![XMouse Settings](/Readme/Images/xmouse_2.png?raw=true)

# Cool Scripts
Here is a list of some of the **most useful** scripts:
* [nUE4CollisionRenaming.pl](#nUE4CollisionRenaming)
* [nUpdateSymmetryOffset.py](#nUpdateSymmetryOffset)

<a id="nUE4CollisionRenaming"/>

# nUE4CollisionRenaming.pl
Rename every hidden & direct child (or sibling, depending on the selection) according to [Unreal Engine 4 collision naming convention.](https://docs.unrealengine.com/latest/INT/Engine/Content/FBX/StaticMeshes/index.html#collision)

	UCX_[RenderMeshName]_##

![nUE4CollisionRenaming](/Readme/Images/nUE4CollisionRenaming.png?raw=true)

<a id="nUpdateSymmetryOffset"/>

# nUpdateSymmetryOffset.py
Update the symmetry Offset according to the bounding box of the current mesh. Really useful when you want a custom pivot or when you have multiple groups of polygons.

![Standard symmetry](/Readme/Images/nUpdateSymmetryOffset_1.png?raw=true)

Note the circled pivot.

![After using the script](/Readme/Images/nUpdateSymmetryOffset_2.png?raw=true)
