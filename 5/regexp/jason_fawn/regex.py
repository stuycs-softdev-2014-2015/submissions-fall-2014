import re


data = open("15414.txt", "r")
text = data.read()
data.close()

fname = open("firstnames.txt", "r")
firstnames = []
for line in fname:
    firstnames.append(line.split()[0].capitalize())
fname.close()

t = open("titles.txt","r")
titles = t.read()
t.close()

for line in titles:
	firstnames.append(line)

'''
lname = open("lastnames.txt", "r")
last = lname.read()
lname.close()
'''
def cleanUp(list):
    newlist = []
    for thing in list:
        if thing not in newlist: 
            newlist.append(thing)    
    return newlist

names = []
def findNames(s):
    matchNames = re.findall(r'([A-Z][a-z.-]+ [A-Z][a-z.-]+)', s)
    ifName(matchNames)
    matchNames = re.findall(r'([A-Z][a-z.-]+ [A-Z][a-z.-]+ [A-Z][a-z.-]+)', s)
    ifName(matchNames)    
    print cleanUp(names)
    #print (names)

def ifName(l):
    for name in l:
        if name.split()[0] in firstnames:
            names.append(name)


	
if __name__=="__main__":
    findNames(text)
