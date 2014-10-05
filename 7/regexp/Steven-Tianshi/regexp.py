import re

f = open("metamorphosis.txt")
s = f.read()
f.close()

def check(s):
    for e in exempt:
        if (s == e):
            return True
    return False

stuff = re.findall("(Mr\.|Ms\.|Mrs\.|Mr|Ms|Mrs) ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)",s)
stuff2 = re.findall("[^\.\?!] ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)",s)
exempt = ["Mr.","Ms.","Mrs.","Mr","Mrs","Ms"]
[stuff2.remove(x) for x in stuff2 if (check(x))]
stuff.extend(stuff2)
print stuff


