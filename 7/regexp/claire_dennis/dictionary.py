import re

firstname_file = open("firstnames.csv")
firstname_text = firstname_file.read()
firstname_file.close()

firstnames = re.findall('[A-Z][A-Z]+',firstname_text,flags=0)

lastname_file = open("lastnames.csv")
lastname_text = lastname_file.read()
lastname_file.close()

lastnames = re.findall('[A-Z][A-Z]+',lastname_text,flags=0)

if __name__=="__main__":
    numfirst = 0;
    for x in firstnames:
        numfirst+=1
    numlast = 0;
    for x in lastnames:
        numlast+=1
    print "number of first names:" + str(numfirst)
    print "number of last names:" + str(numlast)
