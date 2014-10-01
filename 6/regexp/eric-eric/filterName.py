import re

def getNames(s):
    names = re.findall(r"[A-Z][a-z]re+ [A-Z][a-z]re+",s)
    return names

