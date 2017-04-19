# perl

my $selectedMesh = lxq("query sceneservice selection ? locator");
my $numChild = lxq("query sceneservice item.numChildren ? {$selectedMesh}");

my $parent = null;
my @siblings = null;
my $parentName = null;

if($numChild > 0)
{
	fromMesh();
}
else 
{
	fromCollision();
}

#Restore the previous selection after the work is done
lx("select.drop item");
lx("select.subItem {$selectedMesh}");

sub fromCollision
{
	$parent = lxq("query sceneservice item.parent ? $selectedMesh");
	@siblings = lxq("query sceneservice item.children ? $parent");
	$parentName = lxq("query sceneservice item.name ? $parent");

	renameItems();
}

sub fromMesh
{
	@siblings = lxq("query sceneservice item.children ? $selectedMesh");
	$parentName = lxq("query sceneservice item.name ? $selectedMesh");
	renameItems();
}

sub renameItems
{
	my $index = 0;
	my $newName = "None";

	foreach my $sibling (@siblings)
	{
		#Skip visible layers
		if(lxq("layer.setVisibility {$sibling} ?") != false)
		{
			next;
		}

		#Set the name to something generic to avoid duplicated names after second loop
		lx("item.name name:TempName item:{$sibling}");
	}

	foreach my $sibling (@siblings)
	{
		lx("select.subItem [$sibling]");

		#Skip Custom names
		if(lxq("layer.setVisibility {$sibling} ?") != false)
		{
			next;
		}

		if($index < 10)
		{
			$newName = "UCX_".$parentName."_0".$index;
		}
		else
		{
			$newName = "UCX_".$parentName."_".$index;
		}

		lx("item.name name:{$newName} item:{$sibling}");
		$index += 1;
	}
}