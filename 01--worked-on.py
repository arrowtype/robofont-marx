# menuTitle : 01: Worked On
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited.
"""

markSettings = {
    "firstIteration": (0, 1, 0.25, 0.1),        # 1
    "midIteration": (0, 0.5, 0.125, 0.425),
    "lastIteration": (0, 0.25, 0.075, 0.75),
    "maxIterations": 20,
}

f = CurrentFont()

if "maxIterations" in f.lib:
    maxIterations = f.lib["maxIterations"]
else:
    f.lib.update({"maxIterations": markSettings["maxIterations"]})
    maxIterations = f.lib["maxIterations"]

print("maxIterations is: ", str(maxIterations))


start = markSettings["firstIteration"]
middle = markSettings["midIteration"]
end = markSettings["lastIteration"]


def interp(a, b, f):
    interpVal = a+f*(b-a)
    if interpVal < 1:
        return a+f*(b-a)
    else:
        return 1


def updateGlyphMark(glyph, factor):
    if factor < 0.5:
        # increment iterations
        print("less than halfway")
        glyph.lib.update({"numberOfIterations": iterations + 1})

        # generate factor with halfway point
        factor = iterations / (maxIterations / 2)

        glyph.mark = (interp(start[0], middle[0], factor), interp(start[1], middle[1], factor), interp(
            start[2], middle[2], factor), interp(start[3], middle[3], factor))
        print(glyph.mark)

    elif factor >= 0.5:
        print("more than halfway")
        glyph.lib.update({"numberOfIterations": iterations + 1})

        factor = (iterations - maxIterations/2) / (maxIterations/2)
        glyph.mark = (interp(middle[0], end[0], factor), interp(middle[1], end[1], factor), interp(
            middle[2], end[2], factor), interp(middle[3], end[3], factor))
        print(glyph.mark)


for glyphName in f.selection:

    glyph = f[glyphName]

    if "numberOfIterations" not in glyph.lib:
        glyph.mark = markSettings["firstIteration"]

        glyph.lib.update({"numberOfIterations": 1})

        if "iteratedGlyphs" not in f.lib:
            f.lib.update({"iteratedGlyphs": [glyphName]})
        else:

            iteratedGlyphsList = f.lib["iteratedGlyphs"]

            iteratedGlyphsList.append(glyphName)

            f.lib.update({"iteratedGlyphs": iteratedGlyphsList})

    elif glyph.lib["numberOfIterations"] < maxIterations:
        iterations = glyph.lib["numberOfIterations"]
        print("iterations: " + str(iterations))

        factor = iterations / maxIterations

        updateGlyphMark(glyph, factor)

    else:

        newMax = maxIterations + 1

        print("boosting max iterations to " + str(newMax))

        f.lib.update({"maxIterations": newMax})

        iterations = glyph.lib["numberOfIterations"]
        print("iterations: " + str(iterations))

        factor = iterations / newMax

        updateGlyphMark(glyph, factor)

        # TODO: update relative marks of all WIP glyphs?

        for iterGlyph in f.lib["iteratedGlyphs"]:

            iterations = f[iterGlyph].lib["numberOfIterations"]
            factor = iterations / newMax

            updateGlyphMark(f[iterGlyph], factor)
