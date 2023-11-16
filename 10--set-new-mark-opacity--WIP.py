"""
    Get the mark color of currently-selected glyphs and change the 
    opacity of it in the current font.
    
    Useful for changing the Font View to a "dark theme," where 
    the wrong mark opacity can suddenly disrupt a system of colors.
"""

f = CurrentFont()

markOpacity = 0.375

colorToEdit = f[f.selection[0]].markColor
newColor = tuple([c[1] for c in enumerate(colorToEdit) if (c[0] < 3)] + [markOpacity])

print(newColor)

for g in f:
    if g.markColor == colorToEdit:
        g.markColor = newColor
        