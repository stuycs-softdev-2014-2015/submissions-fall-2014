import re
f = open("doc.txt",'r')
doc = f.read()
f.close()

allnames = re.findall('[A-Z][a-z]{2,}(?: [A-Z][a-z]+)?',doc) #gets all capital words/names
titles = re.findall('(?:Mr. |Ms. |Mrs. |Dr. )[A-Z][a-z]+',doc) #gets all names with a title

g = open("names.csv", 'r')
doc2 = g.read()
g.close()
namefile = doc2.split("\r")[1:]

#gets all the last names that follow the first names
lastnames = [t.split(' ')[1] for t in allnames if len(t.split(' ')) == 2 and t.split(' ')[0] in namefile]     

#compiles all the names
found = [n for n in allnames if n.split(' ')[0] in namefile or n in lastnames]   

for z in titles:
    found.append(z)

#tallies up all names
nameCount = {w:found.count(w) for w in found}

print(nameCount)
