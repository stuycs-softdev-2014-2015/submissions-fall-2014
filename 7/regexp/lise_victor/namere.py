import re

textfile = open("names.csv", "r")
names= textfile.read()
textfile.close()
names= names.split()

fname="testfile.txt"

def opentestfile(fname):
    f = open (fname, "r")
    x= f.read () 
    f.close ()
    return x




#x = "Cats are smarter than dogs. This is the opinion of Alex."
#x = "abcdef"
#x = "Mr. Stone found little Amy in Mr. Eric Smith 65364562345243523"
x = opentestfile(fname)
def findname():
    '''
    m= re.search(r".[^ab]+",x) #bcdef
    m= re.search(r"[a-f]+",x) #abcdef
    '''
    m = re.findall("[A-Z][a-z]+",x)
    #m = re.findall("[A-Z][a-z\./].+",x)
    #m = re.findall("[^Mr.][A-Z]?[\w.]+ ",x)
    #print m
    #namesfound= []
    #for name in m:
    #    namesfound.append(name)
    
    #m = re.findall("[^Mr.][A-Z]?[\w.]+ ",x)
    matches=[y for y in m if y in names]
    numbnames={}
    for name in matches:
        if name in numbnames:
            numbnames[name]+=1
        else:
            numbnames[name]=1
    return numbnames
    #return matches
    



print findname()
