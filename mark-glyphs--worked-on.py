# menuTitle : Mark 1: Worked On
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited.
"""

from markLib.markGlyphs import markGlyphs, states

f = CurrentFont()
markGlyphs(f, states["workedOn"])
