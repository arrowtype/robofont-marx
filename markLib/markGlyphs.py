'''
  Setup for other scripts
'''

from markLib.settings import markSettings


def markGlyphs(font, color):
    print("---\n")
    state = list(markSettings.keys())[list(markSettings.values()).index(color)]
    print(f"mark glyphs as: {state} – {str(color)}")

    for g in font.selection:
        print(g)
        font[g].markColor = color
        font[g].lib.update({"com.arrowtype.glyphMarkStatus": state})
    print("---\n")
