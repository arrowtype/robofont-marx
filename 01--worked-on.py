# menuTitle : 01: Worked On (iterate mark)
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited.
"""

iterationMarkSettings = {
    "firstIteration": (0, 1, 0.25, 0.1),
    "midIteration": (0, 0.5, 0.125, 0.425),
    "lastIteration": (0, 0.4, 0.3, 0.65),
    "maxIterations": 20,
}

start = iterationMarkSettings["firstIteration"]
middle = iterationMarkSettings["midIteration"]
end = iterationMarkSettings["lastIteration"]

f = CurrentFont()


def setUpFont(font):
    if "com.arrowtype.maxIterations" in font.lib:
        maxIterations = font.lib["com.arrowtype.maxIterations"]
    else:
        font.lib.update(
            {"com.arrowtype.maxIterations": iterationMarkSettings["maxIterations"]})
        maxIterations = font.lib["com.arrowtype.maxIterations"]


def interp(a, b, f):
    interpVal = a+f*(b-a)
    if interpVal < 1:
        return a+f*(b-a)
    else:
        return 1


def setIterationMarks(font):
    for iterGlyph in font.lib["com.arrowtype.iteratedGlyphs"]:
        iterations = font[iterGlyph].lib["com.arrowtype.numberOfIterations"]
        maxIterations = font.lib["com.arrowtype.maxIterations"]
        factor = iterations / maxIterations

        updateGlyphMark(font[iterGlyph], factor, iterations, maxIterations)


def updateGlyphMark(glyph, factor, iterations, maxIterations):
    if factor < 0.5:

        # generate factor with halfway point
        factor = iterations / (maxIterations / 2)

        glyph.mark = (interp(start[0], middle[0], factor), interp(start[1], middle[1], factor), interp(
            start[2], middle[2], factor), interp(start[3], middle[3], factor))

    elif factor >= 0.5:
        factor = (iterations - maxIterations/2) / (maxIterations/2)
        glyph.mark = (interp(middle[0], end[0], factor), interp(middle[1], end[1], factor), interp(
            middle[2], end[2], factor), interp(middle[3], end[3], factor))


def markSelectedGlyphs(font, selection):
    for glyphName in selection:

        glyph = f[glyphName]

        maxIterations = font.lib["com.arrowtype.maxIterations"]

        iterations = 1

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

            glyph.lib.update(
                {"com.arrowtype.numberOfIterations": iterations + 1})

            updateGlyphMark(glyph, factor, iterations, maxIterations)

        else:

            newMax = maxIterations + 1

            print("boosting max iterations to " + str(newMax))

            font.lib.update({"com.arrowtype.maxIterations": newMax})

            iterations = glyph.lib["com.arrowtype.numberOfIterations"]

            factor = iterations / newMax

            updateGlyphMark(glyph, factor, iterations, maxIterations)

            setIterationMarks(f)

        print(f"/ {glyphName} iterations: {str(iterations)}")


setUpFont(f)
markSelectedGlyphs(f, f.selection)
