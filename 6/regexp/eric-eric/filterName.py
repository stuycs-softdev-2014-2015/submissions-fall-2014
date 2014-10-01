import re

def getNames(s):
    names = re.findall(r"[A-Z][a-z]+ [A-Z][a-z]+",s)
    return names

