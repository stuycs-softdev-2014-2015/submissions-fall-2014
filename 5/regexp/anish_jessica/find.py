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

s2 = []

for w in s:
    s2.append(w.strip("\n"))

#print s2

s3 = []

for w in s2:
    #w = w.strip("\n")
    if not (w in dic):
        #print w
        s3.append(w)
    #print w

#print s3

s4 = [] 

for w in s3:
    if not ("'" in w) and not ("I" == w):
        s4.append(w)

print s4

d.close 


