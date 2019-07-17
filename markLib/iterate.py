'''
  Setup for increment/decrement scripts
'''

from markLib.settings import iterationMarkSettings

start = iterationMarkSettings["firstIteration"]
end = iterationMarkSettings["lastIteration"]


def interp(a, b, f):
    interpVal = a+f*(b-a)
    if interpVal <= 1 and interpVal >= 0:
        return interpVal
    elif interpVal > 1:
        return 1
    else:
        return 0


def updateGlyphMark(glyph, factor, iterations, maxIterations):
    factor = iterations / maxIterations

    glyph.mark = (interp(start[0], end[0], factor), interp(start[1], end[1], factor), interp(
        start[2], end[2], factor), interp(start[3], end[3], factor))


def reportIterations(glyph):
    iterations = glyph.lib["com.arrowtype.numberOfIterations"]
    print(f"/{glyph.name} iterations: {str(iterations)}")
