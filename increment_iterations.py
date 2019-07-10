# menuTitle : Increment Iterations - Darker Teal
# shortCut  : command+control+shift+=
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited. Increments "iterations" 
  value by 1 and makes teal glyph mark slightly darker.
"""

from markLib.iterate import *


f = CurrentFont()
f.lib.update(
    {"com.arrowtype.maxIterations": iterationMarkSettings["maxIterations"]})


def setIterationMarks(font):
    for iterGlyph in font.lib["com.arrowtype.iteratedGlyphs"]:
        iterations = font[iterGlyph].lib["com.arrowtype.numberOfIterations"]
        maxIterations = font.lib["com.arrowtype.maxIterations"]
        factor = iterations / maxIterations

        updateGlyphMark(font[iterGlyph], factor, iterations, maxIterations)


def markSelectedGlyphs(font, selection):
    for glyphName in selection:

        glyph = f[glyphName]

        glyph.lib.update({"com.arrowtype.glyphMarkStatus": "workInProgress"})

        maxIterations = font.lib["com.arrowtype.maxIterations"]

        iterations = 0

        if "com.arrowtype.numberOfIterations" not in glyph.lib:
            glyph.mark = iterationMarkSettings["firstIteration"]

            glyph.lib.update({"com.arrowtype.numberOfIterations": 1})

            if "iteratedGlyphs" not in font.lib:
                font.lib.update({"com.arrowtype.iteratedGlyphs": [glyphName]})
            else:

                iteratedGlyphsList = font.lib["com.arrowtype.iteratedGlyphs"]

                iteratedGlyphsList.append(glyphName)

                font.lib.update(
                    {"com.arrowtype.iteratedGlyphs": iteratedGlyphsList})

        elif glyph.lib["com.arrowtype.numberOfIterations"] < maxIterations:
            iterations = glyph.lib["com.arrowtype.numberOfIterations"]

            factor = iterations / maxIterations

            updateGlyphMark(glyph, factor, iterations, maxIterations)

        else:

            newMax = maxIterations + 1

            print("boosting max iterations to " + str(newMax))

            font.lib.update({"com.arrowtype.maxIterations": newMax})

            iterations = glyph.lib["com.arrowtype.numberOfIterations"]

            factor = iterations / newMax

            updateGlyphMark(glyph, factor, iterations, maxIterations)

            setIterationMarks(f)

        glyph.lib.update(
            {"com.arrowtype.numberOfIterations": iterations + 1})

        reportIterations(glyph)


markSelectedGlyphs(f, f.selection)
