import re

#Titles
#After periods
#Two capital letters in a row

f = open('dorian gray.txt', 'r')
data = f.read()
f.close()

#titles = ["Mrs. ", "Ms. ", "Miss ", "Mr. ", "Dr. ", "Lord ", "Queen ", "King ", "Sir "]
#def name_by_title(data):
#    return re.findall("titles ([A-Z][a-z]+)", data)
def findnames(data):
    return re.findall("([A-Z][a-z]+)[\s-]?([A-Z][a-z]+)?" , data)
def fullnames(data):
    names = findnames(data)
    fullnames = []
    for name in names:
        if not (name[1] == ""):
            fullnames.append([name[0], name[1]])
    return fullnames

#print name_by_title(data)
#print findnames(data)
print fullnames(data)
