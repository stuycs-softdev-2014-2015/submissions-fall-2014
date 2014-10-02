#f = open ('names.txt', 'r')
#n = open ('newnames.txt', 'w')
#i = 1
#for line in f: 
#    if i % 2 == 0:
#       n.write(line)
#       # print line
#    i = i + 1
#
#f.close()
#n.close()

import re

f = open ('newnames.txt', 'r')
for line in f:
    t = line.split (" ")
    t = t [1:]
    te = ""
    for e in t:
        if e[0] == "(":
            break
        te = te + " " +  e
    print te [1:]
f.close
