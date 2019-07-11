# menuTitle : 05: Built from Components - Blue
# shortCut  : command+control+shift+5
"""
  Mark currently-selected glyphs as a "non-exporting component,"
  so it's clear that it shouldn't be directly included in an output font.
"""

from markLib.markGlyphs import markGlyphs, markSettings

f = CurrentFont()
markGlyphs(f, markSettings["fromComponents"])
