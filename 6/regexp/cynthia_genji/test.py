import string
import re
import unittest

#class TestDemo(unittest.TestCase)

berries = open("berry.txt",'r').read().replace("\n","")

names = []


def readNames():
    namematch = re.findall("^[A-Z][a-z]$",berries)
    print namematch
    #namematch.group()

if __name__ == "__main__":
    readNames()
