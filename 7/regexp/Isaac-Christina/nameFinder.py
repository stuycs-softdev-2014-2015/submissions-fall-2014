import re

full = open('names.txt', 'r').readlines()


def getNames(text):
    names = []
    exp = '\s[A-Z]\w+\s[A-Z]\w+'
    for i in text:
        names += re.findall(exp, i)
    return names



if __name__ == "__main__":
    names = getNames(full)
    print names
