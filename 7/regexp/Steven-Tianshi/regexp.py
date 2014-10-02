import re

f = open("metamorphosis.txt")
s = f.read()
f.close()

stuff = re.findall("(Mr\.|Ms\.|Mrs\.) ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)",s)
stuff.append(re.findall("[^\.\?!] ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)",s))
print stuff
