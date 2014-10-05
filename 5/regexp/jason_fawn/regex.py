import re


data = open("15414.txt", "r")
text = data.read()
data.close()

fname = open("firstnames.txt", "r")
firstnames = []
for line in fname:
    firstnames.append(line.split()[0].capitalize())
fname.close()

lname = open("lastnames.txt", "r")
lastnames = []
for line in lname:
    lastnames.append(line.split()[0].capitalize())
lname.close()

t = open("titles.txt","r")
titles = t.read()
t.close()
for line in titles:
	firstnames.append(line)

names = []

def cleanUp(list):
    newlist = []
    for thing in list:
        if not thing in newlist: 
            newlist.append(thing)   
    return newlist

def findNames(s):
    matchNames = re.findall(r"([A-Z][a-z]+ [A-Z][a-z]+)", s)
    ifName(matchNames)
    matchTitle = re.findall(r"([A-Z][a-z.]+ [A-Z][a-z]+[ -][A-Z][a-z]+)", s)
    ifName(matchTitle)
    matchInitial = re.findall(r"([A-Z][a-z]+ [A-Z]. [A-Z][a-z]+)", s)
    ifName(matchInitial)
    matchFull = re.findall(r"([A-Z][a-z.]+ [A-Z][a-z.]+[ -][A-Z][a-z.]+[ -][A-Z][a-z]+)", s) 
    ifName(matchFull)   
    print (cleanUp(names))


def ifName(l):
    for name in l:
        s = name.split()
        if s[0] in firstnames:
            names.append(name)
        if s[0] in titles:
            if s[1] in firstnames or s[1] in lastnames:
                names.append(name)


	
if __name__=="__main__":
    findNames(text)
