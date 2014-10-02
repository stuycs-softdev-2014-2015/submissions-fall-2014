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
last = lname.read()
lname.close()

#firstnames = re.findall(r'[A-Z][a-z]', first)

names = []
def findNames(s):
    matchNames = re.findall(r'([A-Z][a-z.-]+ [A-Z][a-z.-]+)', s)
    ifName(matchNames)
    matchNames = re.findall(r'([A-Z][a-z.-]+ [A-Z][a-z.-]+ [A-Z][a-z.-]+)', s)
    ifName(matchNames)     
    print names

def ifName(l):
    for name in l:
        if name.split()[0] in firstnames:
            names.append(name)

            
findNames(text)
