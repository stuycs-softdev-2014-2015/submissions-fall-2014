import re


def getNames(s):
    names = re.findall(r"[A-Z][a-z'-]+ [A-Z][a-zA-Z'-]+", s)
    return names


def deleteDuplicates(names):
    """Deletes Duplicates and return a Dictionary of names to frequency"""
    D = {}

    for name in names:
        if name in D:
            D[name] += 1
        else:
            D[name] = 1

    return D
