import re
<<<<<<< HEAD
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
=======

File = open('sample.txt', 'r')
book = File.readlines()
file.close

def find_names(x):
    re.search('[A-Z]{1}[a-z]+/s[A-Z]{1}[a-z]+',x)


if __name__ == "__main__":
    find_names(book)
>>>>>>> 233d12b537931f83f19d3eed30401dc503c19c91
