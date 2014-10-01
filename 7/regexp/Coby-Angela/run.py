import string
import re
import unittest

nytimes = open("nytimes.txt",'r').read().replace("\n"," ")

def readTimes():
    allNames = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",nytimes)
    smith = re.findall("[A-Z][a-z]+\sSmith",nytimes)
    print smith

if __name__ == "__main__":
    readTimes()
