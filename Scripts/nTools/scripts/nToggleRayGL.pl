# perl

if (@ARGV == 1)
{
	toggleRayGL(@ARGV[0]);
}
else
{
	lx("view3d.rayGL off");
}

sub toggleRayGL
{
	if(lxq("view3d.rayGL ?") ne @_[0])
	{
		lx("view3d.rayGL @_[0]");
		lx("pref.value opengl.gridVisibility false");
	}
	else
	{
		lx("view3d.rayGL off");
	}
}