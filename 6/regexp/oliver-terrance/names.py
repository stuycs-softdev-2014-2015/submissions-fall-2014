import re

def findnames(d):
    f=open(d,'r')
    data = f.read()
    fullnames=re.findall('[A-Z]\w+ [A-Z]\w+', data)
    titles=re.findall("(?:Dr|Mr|Mrs|Ms|Prof)\.[A-Z]\w+",data)
    f.close()
    return fullnames + titles
    


print findnames("corpus.txt")

