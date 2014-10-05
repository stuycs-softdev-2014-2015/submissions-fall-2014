import re, pickle,sys


filename = sys.argv[1]

f = open(filename+'.txt','r')
g = f.read()
f.close()

h = open('diction.txt','rb')
d= pickle.load(h)
h.close()


def notname(lis):
    x=0
    for sub in lis:
        if sub in d:
            #print sub
            pass
            x=x+1
            #print x
        if x==2: 
            return True
    return False

def stringify(L):
    s = ""
    for n in L:
        for sub in n:
            s = s+" "+sub
        s=s+","
    return s[:-1]

def findnames():
    p = re.compile('(?:[A-Z][a-z].\.)* (?:[A-Z][a-z]+)(?:\s[A-Z][a-z]+)+')
    L=p.findall(g)
    x=0
    for i in xrange(len(L)):
        L[i] = L[i].replace('\n',' ')
        L[i] = L[i].lower().split(" ")
    #print stringify(L)

    L[:] = [ o for o in L if notname(o)==False]
    return L  

print stringify(findnames())
