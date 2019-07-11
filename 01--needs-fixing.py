# menuTitle : 01: Needs Fixing - Red
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "Needs Fixing,"
  so it's clear they should be fixed later.
"""

from markLib.markGlyphs import markGlyphs, markSettings

f = CurrentFont()
markGlyphs(f, markSettings["needsFixing"])
