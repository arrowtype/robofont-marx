# menuTitle : Override & update global RoboFont mark settings

import mojo.UI as mui

from markLib.settings import markSettings


def removeExistingTags():
    prefs = mui.exportPreferences()
    markColors = list(prefs['markColors'])
    markColors.clear()
    prefs['markColors'] = markColors
    mui.importPreferences(prefs)


def colorTagExists(tag, prefs):
    colors = list(prefs['markColors'])
    for color in colors:
        code = color[0]
        name = color[1]
        if name == tag:
            return(True)
    return(False)


def appendMarkColor(code, tag):
    prefs = mui.exportPreferences()
    if colorTagExists(tag, prefs):
        return
    colors = list(prefs['markColors'])
    colors.append((code, tag))
    prefs['markColors'] = colors
    mui.importPreferences(prefs)


removeExistingTags()

for color in markSettings:
    markSettings[color]
    appendMarkColor(markSettings[color], color)
