import re

f = open ("script.txt", "r")
f.readline()

s = []

for line in f:
    for word in line.split (" "):
        if (len (re.findall (r'^[A-Z].', word)) != 0):
            s.append (re.sub(r'(\.|\,|--|\?|\!|\'s)', "", word))
f.close



d = open ("corncob_lowercase.txt", "r")
d.readline()
dic = []

for l in d:
    dic.append((l[0].upper() + l[1:]).strip("\n").strip("\r"))


for w in s:
    w = w.strip("\n")
    if (w in dic):
        print w
        s.remove(w)
    #print w


d.close 


