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
    
