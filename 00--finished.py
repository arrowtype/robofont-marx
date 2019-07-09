# menuTitle : 00: Finished (no mark)
# shortCut  : command+control+shift+0
"""
  Mark currently-selected glyphs as "Finished,"
  so it's clear that they need no known work.
"""

from markLib.markGlyphs import markGlyphs, states

color = None

f = CurrentFont()
markGlyphs(f, states["finished"])
