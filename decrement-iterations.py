# menuTitle : 01b: Decrement Iterations - Blue
# shortCut  : command+control+shift+,
"""
  Decrements "iterations" value by 1 and makes teal glyph mark slightly lighter.
"""

from increment_iterations.py import updateGlyphMark, iterationMarkSettings
f = CurrentFont()
maxIterations = iterationMarkSettings["maxIterations"]


f.lib.update(
    {"com.arrowtype.maxIterations": maxIterations})


def decrementSelectedGlyphs(font, selection):
    for glyphName in selection:

        glyph = font[glyphName]

        if "com.arrowtype.numberOfIterations" in glyph.lib and glyph.lib["com.arrowtype.numberOfIterations"] > 0:

            glyph.lib.update(
                {"com.arrowtype.numberOfIterations": iterations - 1})

            iterations = glyph.lib["com.arrowtype.numberOfIterations"]

            factor = iterations / maxIterations

            updateGlyphMark(glyph, factor, iterations, maxIterations)


decrementSelectedGlyphs(f, f.selection)
