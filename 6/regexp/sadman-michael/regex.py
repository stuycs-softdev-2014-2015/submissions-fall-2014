import re

str = "There was a boy named Billy. John Joe likes cake. The dog likes food. George brings the dog his food. Googles Ceo owns the company"

strbook = open("tale.txt", "r")
strbook1 = strbook.read()
strbook.close()

ex=open("title.txt","r")
ex1=ex.readlines()
ex.close()



results = re.findall("([A-Z][a-z]+)\s([A-Z][a-z]+)", strbook1)

names = ''
def notlist(x,d):
    for l in x:
        if d  in l:
            return False
    return True
for x in results:
    if notlist(ex1,x[0])== True:
        names+=(x[0]+"-"+x[1]+" ")
               
print names



    
