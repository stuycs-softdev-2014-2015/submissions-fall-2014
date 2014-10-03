import re

f = open('in.txt','r')
g = f.read()
f.close()


def makedict():
    s= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    words = []
    for n in s:
        t = open("dict/" + n + " Words.csv")
        r = t.readlines()
        for i in xrange(len(r)-1):
            r[i] = r[i][:-1]
        words.extend(r)
        
        t.close()
   
        
   
    return words

d= makedict()

def findnames():
    p = re.compile('[A-Z][a-z]+\.*(?:\s[A-Z][a-z]+)+')
    L=p.findall(g)
    for i in xrange(len(L)):
        L[i] = L[i].replace('\n',' ')
        L[i] = L[i].lower().split(" ")
    for n in L:
        for sub in n:
            if sub in d:
                pass
            else:
                break
                
    return L  

print findnames()
