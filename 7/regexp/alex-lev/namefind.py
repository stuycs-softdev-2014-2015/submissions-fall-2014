import re
f = open("doc.txt",'r')
doc = f.read()
f.close()
m = re.findall('(?:[^\.\?] )((?:Mr. )?(?:Ms. )?(?:Mrs. )?[A-Z][a-z]+(?: [A-Z][a-z]+)?)',doc)

g = open("names.txt", 'r')
doc2 = g.read()
g.close()
names = doc2.split("\n")

sentences = doc.split('.')
for s in sentences:
    if s.split(' ')[1] in names:
        print(s.split(' '))
        if s.split(' ')[1][0].isupper():
            m.append(s.split(' ')[0] + ' ' + s.split(' ')[1])
        else:
            m.append(s.split(' ')[0])



print(m)
