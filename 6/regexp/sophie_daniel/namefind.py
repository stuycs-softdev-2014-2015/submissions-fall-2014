import re
f=open("first.txt",'r')
s=f.read()
#p=re.compile("(([A-Z][a-z]*)\s([A-Z][a-z]*))")
#p=re.compile("([A-Z][a-z]*\s*){2,}")
p=re.compile("(([A-Z][a-z]*)\s([A-Z][a-z]*))")
#print p.findall(s)
r=re.compile("(?<!\.\s)([A-Z][a-z]+)")
print r.findall(s)
