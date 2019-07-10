# menuTitle : 02: Needs Feedback
# shortCut  : command+control+shift+2
"""
  Mark currently-selected glyphs as "waiting on critique,"
  so it's clear what a collaborate should critique.
"""

from markLib.markGlyphs import markGlyphs, markSettings

f = CurrentFont()
markGlyphs(f, markSettings["waitingForCritique"])
