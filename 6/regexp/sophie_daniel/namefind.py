import re
def nameFind(fil):
    f=open(fil,'r')
    s=f.read()
    f.close()
    #p=re.compile("(([A-Z][a-z]*)\s([A-Z][a-z]*))")
    #p=re.compile("([A-Z][a-z]*\s*){2,}")
    p=re.compile("([A-Z][a-z]*)\s([A-Z][a-z]*)")
    pre= p.findall(s)  
    r=re.compile('((?<![\.\!\?\"])(?<![\.\!\?\"\:\;]\s)(?<![\.\!\?\"\;\:]\s\s)[A-Z][a-z]+)')
    l=r.findall(s)
    for f in pre:
        for se in f:
            l.append(se)
    d={name: s.count(name) for name in l}
    #for name in r.findall(s):
    #    print name+":" +str(s.count(name))
    return d
print nameFind('first.txt')
