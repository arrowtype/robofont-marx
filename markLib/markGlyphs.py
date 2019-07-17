'''
  Setup for other scripts
'''

markSettings = {
    "fix": (1.0, 0.65, 0.65, 1),
    "check": (1, 1, 0, 1),
    "experiment": (0.65, 0, 1, 1),
    "nonexporting": (0.5, 0.5, 0.5, 1),
    "composed": (0.75, 0.75, 0.75, 1),
    "finished": (1, 1, 1, 1),
}


def markGlyphs(font, color):
    print("---\n")
    state = list(markSettings.keys())[list(markSettings.values()).index(color)]
    print(f"mark glyphs as: {state} – {str(color)}")

    for g in font.selection:
        print(g)
        font[g].markColor = color
        font[g].lib.update({"com.arrowtype.glyphMarkStatus": state})
    print("---\n")
