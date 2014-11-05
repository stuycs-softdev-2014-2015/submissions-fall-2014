import re
import unittest
import string

tales = open("sample.txt", 'r').read().replace("\r\n\r\n", "").replace("\r", "").replace("\r\n","").replace("\n", "")

names = []
firstnames = []

def findname():
    fullnames = re.findall("[A-Za-z]*\s([A-Z][a-z]*\s[A-Z][a-z]*)", tales)
    for i in fullnames:
        if i not in names and len(i) > 3:
            names.append(i)

    fnames = re.findall("[A-Za-z]*\s([A-Z][a-z]*)", tales)
    for i in fnames:
        if i not in fnames:
            firstnames.append(i)

    print names


if __name__=="__main__":
    findname()
