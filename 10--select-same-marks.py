# menuTitle : Select all glyphs with selected mark
# shortCut  : command+control+shift+F
"""
  Select glyphs of one or more mark colors, then 
  use this script to select all glyphs with the same marks.
"""

f = CurrentFont()

print(f.selection)

markColors = []

for g in f.selection:
    mark = f[g].mark
    print(mark)
    markColors.append(mark)

for g in f:
    if g.mark in markColors:
        print(g.name)
        g.selected = True
    