'''
  Setup for other scripts
'''

states = {
    "firstIteration": (0, 1, 0.25, 0.1),                # 1
    "midIteration": (0, 0.5, 0.25, 0.65),
    "lastIteration": (0, 0, 0.25, 1),
    "maxIterations": 20
    "waitingForCritique": (0, 0, 1, 0.75),      # 2
    "experiment": (1, 0, 1, 0.75),              # 3
    "bad": (0.666, 0, 0.125, 0.75),             # 4
    "nonExportingComponent": (0, 0, 0, 0.25),   # 5
    "finished": None,                           # 0
    "fromComponents": (1.0, 0.7, 0.0, 1)
}


def markGlyphs(font, color):
    state = list(states.keys())[list(states.values()).index(color)]
    print(f"mark glyphs as: {state} – {str(color)}")

    for g in font.selection:
        print(g)
        font[g].markColor = color
    print("---\n")
