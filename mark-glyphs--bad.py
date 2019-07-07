# menuTitle : Mark Glyphs: Bad
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "Bad,"
  so it's clear they should be fixed later.
"""

# TODO: find out how to update the "cache" of an imported script
from markGlyphs8 import markGlyphs, states

# "bad" color
# color = (0.666, 0, 0.125, 0.5)

f = CurrentFont()
markGlyphs(f, states["bad"])
