import re


def findnames(d):
    f=open(d,'r')
    data = f.read()
    capital=re.findall('[A-Z]\w+',data)
    fullnames=re.findall('[A-Z]\w+ [A-Z]\w+', data)
    titles=re.findall("(?:Dr|Mr|Mrs|Ms|Prof)\.[A-Z]\w+",data)
    suffixes=re.findall("[A-Z]\w+ (?:Sr|Jr|PhD|MD)\.?",data)
    begofsent=re.findall("(?:\.|\?|\!)\s([A-Z]\w+)",data)
    f.close()
    names=fullnames + titles + suffixes
    unsure=appeared(capital,names)
    for x in capital:
        if not appearwithin(x,names) and x not in begofsent:
            names.append(x)
            if x in unsure:
                unsure.remove(x)
    print "NAMES: "
    print names
    print "UNSURE:"
    print unsure

def appeared(unconf,conf):
    repeat=[]
    uns=[]
    for x in unconf:
        if appearwithin(x,conf):
            repeat.append(x)
    for x in unconf:
        if x not in repeat and x not in uns:
            uns.append(x)
    return uns

def appearwithin(x,group):
    for a in group:
        if x in a:
            return True
    return False


findnames("corpus.txt")

