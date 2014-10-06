import re

f = open('text.txt', 'r')
rawtext = f.read() #test is a string
f.close()

words = rawtext.split()
pairs = []

i = 1
while i < len(words):
    new = words[i-1] + " " +  words[i]
    pairs.append(new.strip(",!?.;:\""))
    i = i + 1

reg = re.compile('[A-Z]([a-z|\-|\'])+ [A-Z]([a-z|\-|\'])+')
names = []

dict = {}
j = 0
while j < len(pairs):
    if ( reg.match(pairs[j]) != None and pairs[j] not in names):
            names.append(pairs[j])
    j = j + 1

k = 0
while k < len(names):
    if ((names[k] + "").find("Dear") > -1 or (names[k] + "").find("College") > -1
        or (names[k] + "").find("University") > -1):
        names.pop(k)
    k = k + 1


print names
