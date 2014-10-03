import re

textfile = open("names.csv", "r")
names= textfile.read()
textfile.close()
names= names.split()

fname="JackWinters.txt"

def opentestfile(fname):
    f = open (fname, "r")
    x= f.read () 
    f.close ()
    return x


x = opentestfile(fname)
x = "Mr. Johnny Deep was loved by Emily J. Jenkino but not Jane Terrance."
def findname():
    '''
    m= re.search(r".[^ab]+",x) #bcdef
    m= re.search(r"[a-f]+",x) #abcdef
    m = re.findall("[A-Z][a-z]+",x)  #gets all capitalized words
    '''
    m = re.findall("[A-Z][a-z|-]+",x) #gets all capitalizes words
    z = re.findall("[A-Z][a-z|'|.|]+ [A-Z][a-z|'|\.]+",x)
    m = re.findall("[A-Z][a-z|'|.|]+ [A-Z][a-z|'|\.]+ [A-Z][a-z|'|\.]+",x)
    print z
    print m
    #build dictionary or list with names (dictionary would be more efficient probably
    matches=[y for y in m if y in names]
    numbnames={}
    for name in matches:
        if name in numbnames:
            numbnames[name]+=1
        else:
            numbnames[name]=1
    
    namesfound= []
    for name in m:
       namesfound.append(name)
    print namesfound
    #return numbnames
    #return matches
    



print findname()
