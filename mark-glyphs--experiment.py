# menuTitle : Mark 3: Experiment
# shortCut  : command+control+shift+3
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited.
"""

from markLib.markGlyphs import markGlyphs, states

f = CurrentFont()
markGlyphs(f, states["experiment"])
