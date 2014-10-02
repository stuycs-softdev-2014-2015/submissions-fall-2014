import re


def getNames(s):
    names = re.findall(r"[A-Z][a-z'-]+ [A-Z][a-zA-Z'-]+", s)
    return names


def getSurnames(s):
    names = re.findall(r"M[a-z]{1,2}\. ([A-Z][a-zA-z'-]+)", s)
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


def splitName(list):
    ans = []
    for element in list:
        current = element.split(" ")

        for word in current:
            ans.append(word)
    return ans


def readText(filepath = "isaac.test"):
    """Returns a list of names from the text file"""
    file = open(filepath, "r")
    text = file.read()
    file.close()

    L = getNames(text)
    L = L + getSurnames(text)
    return L

if __name__ == "__main__":
    print readText()
