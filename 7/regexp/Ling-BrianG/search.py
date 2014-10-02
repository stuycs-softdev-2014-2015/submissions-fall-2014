import re
import unittest
import string

tales = open("sample.txt", 'r').read().replace("\r\n\r\n", "").replace("\r", "").replace("\r\n","").replace("\n", "")

names = []
firstnames = []

def findname():
    fullnames = re.findall("[A-Z][a-z]*\s[A-Z][a-z]*", tales)
    for i in fullnames:
       names.append(i)

    fnames = re.findall("[A-Z][a-z]*", tales)
    for i in fnames:
        firstnames.append(i)

    print fnames


if __name__=="__main__":
    findname()
