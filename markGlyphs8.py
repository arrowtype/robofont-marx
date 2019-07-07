'''
  Setup for other scripts
'''

states = {
    "good": (0.666, 0, 0.125, 0.5),
    "bad": (0.666, 0, 0.125, 0.5)
}


def markGlyphs(font, color):
    print("hello" + str(color))
    for g in font.selection:
        font[g].markColor = color
