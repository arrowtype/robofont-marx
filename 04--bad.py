# menuTitle : 04: Needs Fixing – Red
# shortCut  : command+control+shift+4
"""
  Mark currently-selected glyphs as "Needs Fixing,"
  so it's clear they should be fixed later.
"""

from markLib.markGlyphs import markGlyphs, markSettings

f = CurrentFont()
markGlyphs(f, markSettings["needsFixing"])
