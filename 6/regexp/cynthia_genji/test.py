import string
import re
import unittest

#class TestDemo(unittest.TestCase)

berries = open("berry.txt",'r').read().replace("\n","")

names = []


def readNames():
    n = re.compile("[A-Z][a-z]+\040[A-Z][a-z]+")
    #names = n.match(berries)
    #print names.group()
    names = n.findall(berries)
    print names

if __name__ == "__main__":
    readNames()
