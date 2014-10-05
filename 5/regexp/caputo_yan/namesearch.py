import re

firstnames = open("First_Names.csv", 'r')
lastnames = open("Last_Names.csv", 'r')

firstn = firstnames.read()
firstnames.close()
first = firstn.split(",")

lastn = lastnames.read()
lastnames.close()
last = lastn.split(",")

def gothrough(filename):
    document = open(filename, 'r')
    docopen = document.read()
    document.close()
    regex = re.compile('[A-Z][a-z]+')
    possName = regex.findall(docopen)
    print possName
    final = []
    '''
    for x in possName:
#FOR SOME REASON THIS IS NOT RUNNING...
        if x in first:
            print "iudius"
            final.append(x)
    print final
    '''

if __name__=="__main__":
    gothrough("PrideandPrejudice.txt")
