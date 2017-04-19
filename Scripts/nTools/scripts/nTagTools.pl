# perl

foreach my $arg(@ARGV)
{
	if ($arg eq "tagColor1") {&tagColor1}
	elsif ($arg eq "tagColor2") {&tagColor2}
	elsif ($arg eq "tagColor3") {&tagColor3}
	elsif ($arg eq "tagSmooth1") {&tagSmooth1}
	elsif ($arg eq "tagSmooth2") {&tagSmooth2}
	elsif ($arg eq "tagSmooth3") {&tagSmooth3}
	elsif ($arg eq "tagRemoveColors") {&tagRemoveColors}
	elsif ($arg eq "tagRemoveSmooths") {&tagRemoveSmooths}
	elsif ($arg eq "tagRemoveAll") {&tagRemoveAll}
}

sub tagColor1
{
	tagColor("color1");
}

sub tagColor2
{
	tagColor("color2");
}

sub tagColor3
{
	tagColor("color3");
}

sub tagSmooth1
{
	tagSmooth("smoothSmall");
}

sub tagSmooth2
{
	tagSmooth("smoothMedium");
}

sub tagSmooth3
{
	tagSmooth("smoothLarge");
}

sub tagColor
{
	tagRemoveColors();
	lx("select.editSet @_[0] add");
}

sub tagSmooth
{
	tagRemoveSmooths();
	lx("select.editSet @_[0] add");
}

sub tagRemoveColors
{
	lx("select.editSet color1 remove {}");
	lx("select.editSet color2 remove {}");
	lx("select.editSet color3 remove {}");
}

sub tagRemoveSmooths
{
	lx("select.editSet smoothSmall remove {}");
	lx("select.editSet smoothMedium remove {}");
	lx("select.editSet smoothLarge remove {}");
}

sub tagRemoveAll
{
	tagRemoveColors();
	tagRemoveSmooths();
}