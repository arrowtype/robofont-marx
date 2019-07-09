'''
  Setup for other scripts
'''

states = {
    "workedOn": (0.5, 0, 0.125, 0.125),         # 1
    "waitingForCritique": (0, 0, 1, 0.75),      # 2
    "experiment": (0.75, 0, 1, 0.5),            # 3
    "bad": (0.666, 0, 0.125, 0.5),              # 4
    "nonExportingComponent": (0, 0, 0, 0.25),   # 5
    "finished": (1, 1, 1, 0),                   # 0
    "fromComponents": (1.0, 0.7, 0.0, 1.0)
}


def markGlyphs(font, color):
    print("mark glyphs as: " + list(states.keys())
          [list(states.values()).index(color)])
    for g in font.selection:
        print(g)
        font[g].markColor = color
    print("---\n")
