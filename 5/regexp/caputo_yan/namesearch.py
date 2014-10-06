import re

firstnames = open("First_Names.csv", 'r')
lastnames = open("Last_Names.csv", 'r')
dictionary = open("dictionary.txt", 'r')

firstn = firstnames.read()
firstnames.close()
first = firstn.split("\r")

lastn = lastnames.read()
lastnames.close()
last = lastn.split("\r")

dic= dictionary.read()
dictionary.close()
dicti=dic.split("\n")

names = first + last
def gothrough(filename):
    document = open(filename, 'r')
    docopen = document.read()
    document.close()
    regex = re.compile('[A-Z][a-z]+')
    possName = regex.findall(docopen)
    final = []
    for x in possName:
        if  x.lower() in dicti:
            possName.remove(x)
        elif x in names:
            final.append(x)
            possName.remove(x)
        
#removed +possName
    print final
if __name__=="__main__":
    gothrough("PrideandPrejudice.txt")
