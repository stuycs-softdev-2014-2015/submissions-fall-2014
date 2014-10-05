import re

str = "There was a boy named Billy. John Joe likes cake. The dog likes food. George brings the dog his food. Googles Ceo owns the company"

strbook = open("tale.txt", "r")
strbook1 = strbook.read()
strbook.close()


results = re.findall("([A-Z][a-z]+)\s([A-Z][a-z]+)", strbook1)

names = ''

for x in results:
    #print x[0]
    print x[0]#!= "Our":
#        names.append(results[x])

print names

