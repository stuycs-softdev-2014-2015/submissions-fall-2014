import re

f = open("unprocessednames.txt")
s = f.read()
f.close()

newL = re.findall("[A-Z]+",s)
i = 0
for name in newL:
    newL[i] = name.lower().capitalize()
    i = i + 1

f = open("names.txt",'w')
f.writelines(line + ',' for line in newL)
f.close()


    
