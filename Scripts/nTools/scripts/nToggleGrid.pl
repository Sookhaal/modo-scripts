#perl

my $isGridVisible = lxq("pref.value opengl.gridVisibility ?");
$isGridVisible ^= 1;
lx("pref.value opengl.gridVisibility [$isGridVisible]");