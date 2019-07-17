# menuTitle : 04 Non-Exporting - Gray
# shortCut  : command+control+shift+4
"""
  Mark currently-selected glyphs as a "non-exporting component,"
  so it's clear that it shouldn't be directly included in an output font.
"""

from markLib.markGlyphs import markGlyphs, markSettings

f = CurrentFont()
markGlyphs(f, markSettings["nonexporting"])
