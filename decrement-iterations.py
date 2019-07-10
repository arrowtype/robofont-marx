# menuTitle : Decrement Iterations - Lighter Teal
# shortCut  : command+control+shift+-
"""
  Decrements "iterations" value by 1 and makes teal glyph mark slightly lighter.
"""

from markLib.iterate import *

f = CurrentFont()
maxIterations = iterationMarkSettings["maxIterations"]


f.lib.update(
    {"com.arrowtype.maxIterations": maxIterations})


def decrementSelectedGlyphs(font, selection):
    for glyphName in selection:

        glyph = font[glyphName]

        if "com.arrowtype.numberOfIterations" in glyph.lib and glyph.lib["com.arrowtype.numberOfIterations"] > 0:

            iterations = glyph.lib["com.arrowtype.numberOfIterations"]

            glyph.lib.update(
                {"com.arrowtype.numberOfIterations": iterations - 1})

            factor = iterations / maxIterations

            updateGlyphMark(glyph, factor, iterations, maxIterations)

            reportIterations(glyph)


decrementSelectedGlyphs(f, f.selection)
