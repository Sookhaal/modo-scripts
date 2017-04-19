# perl

foreach $f(@ARGV)
{
	if($f eq "ofSelection")
	{
		ofSelection();
	}
	if($f eq "ofParent")
	{
		ofParent();
	}
}

sub ofSelection
{
	my $selectedMesh = lxq("query sceneservice selection ? locator");
	lx("item.create mesh");

	if($selectedMesh eq "")
	{
		return;
	}

	my $newMesh = lxq("query sceneservice selection ? locator");
	lx("select.subItem {$selectedMesh}");
	lx("item.parent");
	lx("select.drop item");
	lx("select.subItem {$newMesh}");
	lx("itemList.find");
}

sub ofParent
{
	my $selectedMesh = lxq("query sceneservice selection ? locator");
	my $parentMesh = lxq("query sceneservice item.parent ? {$selectedMesh}");
	if($parentMesh eq "")
	{
		ofSelection();
		return;
	}

	lx("select.drop item");
	lx("select.subItem {$parentMesh}");
	ofSelection();
}