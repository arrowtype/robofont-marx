'''
  Setup for other scripts
'''

markSettings = {
    "waitingForCritique": (1, 1, 0, 0.75),      # 2
    "experiment": (0.5, 0, 1, 0.75),              # 3
    "needsFixing": (0.666, 0, 0, 0.75),     # 4
    "nonExportingComponent": (0, 0, 0, 0.5),   # 5
    "finished": None,                           # 0
    "fromComponents": (0, 0.25, 1, 1)
}


def markGlyphs(font, color):
    print("---\n")
    state = list(markSettings.keys())[list(markSettings.values()).index(color)]
    print(f"mark glyphs as: {state} – {str(color)}")

    for g in font.selection:
        print(g)
        font[g].markColor = color
        font[g].lib.update("com.arrowtype.glyphMarkStatus": state)
    print("---\n")
