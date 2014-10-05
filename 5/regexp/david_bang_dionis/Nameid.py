import re

def openfile(filename):
    f=open(filename,"r")
    return f.read()

def fullname(d):
    r= re.findall( "[A-Z][a-z]+ [A-Z][a-z]+", d)
    return r
def titles(d):
    r= re.findall( "[A-Z][a-z][a-z]?\. [A-Z][a-z]+", d)
    return r
def names(d):
    return fullname(d)+titles(d)
for i in names(openfile("test.txt")):
    print i
