# menuTitle : Mark 5: Non-Exporting
# shortCut  : command+control+shift+5
"""
  Mark currently-selected glyphs as a "non-exporting component,"
  so it's clear that it shouldn't be directly included in an output font.
"""

from markLib.markGlyphs import markGlyphs, states

f = CurrentFont()
markGlyphs(f, states["nonExportingComponent"])
