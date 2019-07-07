# menuTitle : Mark Glyphs: Good
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "Bad,"
  so it's clear they should be fixed later.
"""

# TODO: find out how to update the "cache" of an imported script
from markGlyphs3 import markGlyphs

# "good" color
color = (0, 1, 0.125, 0.5)
# color = (0.666, 0, 0.125, 0.5)

f = CurrentFont()
markGlyphs(f, color)
