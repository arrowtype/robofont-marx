'''
  Setup for other scripts
'''

states = {
    "workedOn": (0, 1, 0.25, 1),                # 1
    "waitingForCritique": (0, 0, 1, 0.75),      # 2
    "experiment": (1, 0, 1, 0.75),              # 3
    "bad": (0.666, 0, 0.125, 0.75),             # 4
    "nonExportingComponent": (0, 0, 0, 0.25),   # 5
    "finished": None,                           # 0
    "fromComponents": (1.0, 0.7, 0.0, 1)
}


def markGlyphs(font, color):
    print("mark glyphs as: " + list(states.keys())
          [list(states.values()).index(color)] + " " + str(color))
    for g in font.selection:
        print(g)
        font[g].markColor = color
    print("---\n")
