'''
mr
master
ms
miss
mrs
sir
madam
ma'am
dame
lord
lady
dr
prof

*period optional

dear ...
hi ...
sincerely ...
thanks ...
regards ...
best ...

*comma optional

list comprehension through csvs
pay attention to things after titles
any 2 adjacent first letter capital'd words
things before commas
'''

firstnames = open("First_Names.csv", 'r')
lastnames = open("Last_Names.csv", 'r')

firstn = firstnames.readline()
firstnames.close()
first = firstn.split(",")

lastn = lastnames.readline()
lastnames.close()
last = lastn.split(",")

def gothrough(filename):
    doc = open(filename, 'r')
    docopen = doc.readline()
    doc.close()
    words = docopen.split(" ") #list containing individual words
    found = []
    for w in range(len(found)-1):
        if found[w][0].isupper:
            if True: #check first is true
                if True: #check last is true
                    found.append([w[0],w[1]])
    return found

def 
