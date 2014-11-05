import re
import csv


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
    """Reads from the filepath given and
    Returns a Dictionary of names to frequency from the text file"""
    file = open(filepath, "r")
    text = file.read()
    file.close()

    L = getNames(text)
    L = L + getSurnames(text)
    L = splitName(L)
    D = deleteDuplicates(L)

    falsePositives = readFalsePositives()

    for key in D.keys():
        if key in falsePositives:
            del D[key]

    return D


def readFalsePositives(filepath = "falsePositives"):
    """Reads from the filepath given and
    Returns a set of names from the text file"""
    with open(filepath, 'r') as f:
        text = f.read()
        falsePositives = set()
        for x in text.split(','):
            falsePositives.add(x)
    return falsePositives


class falsePositivesFixer():
    """Class used for prompting the user about false positives and appending
    them to the given filepath"""
    def __init__(self, filepath = "falsePositives"):
        pass

    def appendSelfPositives(self, falsePositivesInput,
                            filepath = "falsePositives"):
        """Writes a string to a file in a csv format

        falsePositivesFixer(iterable, filepath)
        optional parameter filepath
        """
        with open(filepath, 'w') as f:
            s = ','.join(falsePositivesInput)
            f.write(s)

    def run(self, words, filepath = "falsePositives"):
        """Writes string to a file if the user prompts it is a falsepositive

        takes an iterable parameter

        input of y: append to file
        input of n: don't append to file
        """
        falsePositives = readFalsePositives()
        for word in words:
            s = raw_input("Is this a falsepositive? [y or n]: %s"%word)
            if s == "y":
                print "saving to falsepositive set"
                falsePositives.add(word)
            elif s == "n":
                print "keeping word"
            else:
                print "unrecognizable command. Considering it as a no"
        print falsePositives
        return falsePositives

if __name__ == "__main__":
    fixer = falsePositivesFixer()
    L = readText().keys()
    fixer.run(L)
