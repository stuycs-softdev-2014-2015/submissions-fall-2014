import re

full = open('names.txt', 'r').readlines()
first_names = open("CSV_Database_of_First_Names.csv", "r").readlines()
first_names = {x:x for x in first_names}
print first_names

def getNames(text):
    names = []
    exp = '[A-Z]\w+\s[A-Z]\w+'
    for i in text:
        names += re.findall(exp, i)
    return names

def checkNames(names):
    checked_names = []
    for i in names:
        first = i.split(" ")[0]
       
        if first in first_names:
            checked_names += i
    return checked_names
            


if __name__ == "__main__":
    names = getNames(full)
    checked = checkNames(names) 
    print checked
