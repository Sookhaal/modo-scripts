# perl

if(!lxq("query scriptsysservice userValue.isDefined ? nToggleVisibility"))
{
	lx("user.defNew nToggleVisibility type:integer life:temporary");
	lx('user.def nToggleVisibility list "on;off"');
}

if ((lxq("user.value nToggleVisibility ?") eq "") || (lxq("user.value nToggleVisibility ?") eq "on"))
{
	lx("hide.unsel");
	lx("view3d.inactiveInvisible true");
	lx("user.toggle nToggleVisibility on off 0");
}
else
{
	lx("unhide");
	lx("view3d.inactiveInvisible false");
	lx("user.toggle nToggleVisibility off on 0");
}