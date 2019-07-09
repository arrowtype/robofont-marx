# menuTitle : 01: Worked On
# shortCut  : command+control+shift+1
"""
  Mark currently-selected glyphs as "worked on,"
  so it's clear they have been edited.
"""

from markLib.markGlyphs import markGlyphs, states

f = CurrentFont()
# markGlyphs(f, states["workedOn"])

print(f.selection)

for glyphName in f.selection:

    glyph = f[glyphName]

    if "numberOfIterations" not in glyph.lib:
        glyph.mark = states["workedOn"]

        glyph.lib.update({"numberOfIterations": 1})
    else:
        iterations = glyph.lib["numberOfIterations"] + 1
        glyph.lib.update({"numberOfIterations": iterations})

        r, g, b, a = states["workedOn"]

        print(r, g, b, a)

        factor = 0.1

        r = float(r)+(float(r) * iterations * factor)
        g = float(g)+(float(g) * iterations * factor)
        b = float(b)+(float(b) * iterations * factor)
        a = float(a)+(float(a) * iterations * factor)

        glyph.mark = (float(r), float(g)*(1 + iterations * 0.1),
                      float(b), float(a)*(1 + iterations * 0.1))


# store iterations in glyph.lib, then base color on that
