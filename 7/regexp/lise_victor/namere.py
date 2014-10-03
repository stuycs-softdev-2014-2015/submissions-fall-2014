import re

textfile = open("names.csv", "r")
names= textfile.read()
textfile.close()
names= names.split()

fname="JackWinters.txt"

def opentestfile(fname):
    f = open (fname, "r")
    x= f.read() 
    f.close ()
    return x

x = opentestfile(fname)
x = "Mr. Johnny Deep was loved by Emily J. Jenkino but not Jane Terrance."
def findname():
    m = re.findall("[A-Z][a-z|-]+",x) #gets all capitalizes words
    z = re.findall("[A-Z][a-z|'|.|]+ [A-Z][a-z|'|\.]+",x) #
   # matches = re.findall("[A-Z][a-z|'|.|]+ [A-Z][a-z|'|\.]+ [A-Z][a-z|'|\.]+",x)
   
    matches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[\']?[s]?[\s]?)+",x)
   
    numbnames={}
    for name in matches:
        if name in numbnames:
            numbnames[name]+=1
        else:
            numbnames[name]=1
    print matches
    return "DONE SEARCHING"

'''
    namesfound= []
    for name in m:
        if re.search("[\"|\']?(?<=Mr\.|Mrs\.|Ms\.|)([\s]?[A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)+",name)!= None:
           # re.sub("[\"|\']?(?<=Mr\.|Mrs\.|Ms\.|)([\s]?[A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)+",name,"")
            namesfound.append(name)
    namesfound.append(name)


   
    print namesfound
'''

    



print findname()
