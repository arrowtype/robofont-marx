# menuTitle : 03: Experiment - Purple
# shortCut  : command+control+shift+3
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited.
"""

from markLib.markGlyphs import markGlyphs
from markLib.settings import markSettings

f = CurrentFont()
markGlyphs(f, markSettings["experiment"])
