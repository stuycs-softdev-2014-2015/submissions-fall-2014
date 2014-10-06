#!/usr/bin/python

import re

text = open("doctor_who_wiki.txt", "r")
tester = text.read()
text.close()

def getNames( text ):
    names = re.findall( r'[A-Z][a-z]* [A-Z][a-z]*|Mrs?. [A-Z][a-z]*|Dr. [A-Z][a-z]*' , tester)
    return names

def checkFirstNames( allNames )

if __name__ == "__main__":
    result = getNames(tester)
    print result
