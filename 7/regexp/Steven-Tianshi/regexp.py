import re

f = open("prideandprejudice.txt")
s = f.read()
f.close()

f = open("names.txt")
names = f.read()
namesL = names.split(",")
f.close()

def checkNames(L):
    ret = []
    for s in L:
        for name in namesL:
            if (s == name):
                ret.append(s)
    return ret

capitals = re.findall("([A-Z][a-z]*)",s)
"""Old code that has been replaced to find more general words:

stuff = re.findall("(Mr\.|Ms\.|Mrs\.|Mr|Ms|Mrs) ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)",s)
stuff2 = re.findall("[^\.\?!] ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)",s)
exempt = ["Mr.","Ms.","Mrs.","Mr","Mrs","Ms"]
[stuff2.remove(x) for x in stuff2 if (check(x))]
stuff.extend(stuff2)
print stuff
print checkNames(stuff)"""

#print stuff
print checkNames(capitals)

