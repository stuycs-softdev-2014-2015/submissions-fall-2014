import re

f = open('in.txt','r')
g = f.read()
f.close()

def findnames():
    p = re.compile('[A-Z][a-z]+\.*(?:\s[A-Z][a-z]+)+')
    L=p.findall(g)
    for i in xrange(len(L)):
        L[i] = L[i].replace('\n',' ')
    return L  

print findnames()
