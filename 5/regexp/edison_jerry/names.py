#!/usr/bin/python
import re

txt = open("book.txt", "r")
text = txt.read()
txt.close()

firstNames=open("FirstName.csv","r")
fNames=firstNames.read().replace("\n"," ")
firstNames.close()

lastNames=open("LastName.csv","r")
lNames=lastNames.read().replace("\n"," ")
firstNames.close()

def nameFind():
    FNDic = {}
    FirstNames = fNames.split()
    FNDic = dict.fromKeys(FirstNames, FirstNames)

    LNDic={}
    LastNames = lNames.split()
    LNDic = dict.fromKeys(LastNames, LastNames)
    
    match = re.findall( r'[A-Z][a-z]* [A-Z][a-z]* | Mrs?. [A-Z][a-z]* | Dr. [A-Z][a-z]*' , text)

    matches = []
    
    for yay in match:
        full = yay.split()
        if full[0] in FNDic and full[1] in LNDic:
            matches.append(yay)
    
    print matches

if _name_== "_main_":
    nameFind()
