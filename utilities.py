import subprocess

ANSIcolours = {
    "r": "\u001b[31m",
    "g": "\u001b[32m",
    "b": "\u001b[34m",
    "c": "\u001b[36m",
    "m": "\u001b[35m",
    "y": "\u001b[33m",
    "reset": "\u001b[0m",
}

def colourString(astring, colour):
    if not colour in ANSIcolours:
        raise ValueError('Colour not supported')
    return ANSIcolours[colour]+astring+ANSIcolours['reset']

def rainbowString(astring):
    out = ""
    cycle = ['r','y','g','c','b','m']
    for i in range(len(astring)):
        out += colourString(astring[i],cycle[i % 6])
    return out

def prettyList(alist, colourslist):
    width = len(str(max(alist)))
    out = "["
    for i in range(len(alist)):
        if len(colourslist) > i and colourslist[i] is not None:
            out += colourString(str(alist[i]).rjust(width), colourslist[i])
        else:
            out += str(alist[i]).rjust(width)
        out += ', '
    out = out[:-2]
    out += "]"
    return out

def errorText(astring):
    out = ANSIcolours['r'] + "!!! " + astring + " !!!" + ANSIcolours['reset']
    return out

def bannerText(astring, achar):
    _, columns = subprocess.check_output(['stty', 'size']).split()
    out = '{s:{c}^{n}}'.format(s=" "+astring+" ",n=int(columns),c=achar)
    return out
