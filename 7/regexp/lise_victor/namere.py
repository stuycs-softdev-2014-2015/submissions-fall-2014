import re

def opentestfile(fname):
    f = open (fname, "r")
    x= f.read() 
    f.close ()
    return x

names= opentestfile("names.csv");
names= names.split()

fname="JackWinters.txt"


x = opentestfile(fname)
x = "\"Zane said Johnny Aaron Deep was loved by Emily J. Jenkino and Mary but not Jane Terrance but he is also loved by James! "
print x
def findname():
    matches = re.findall("[A-Z][a-z]+",x)

    #matches  ('firstname', 'lastname')
    flmatches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)[\s]([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)",x)
    #matches with middle initials ('firstname','MI','lastname')
    matches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)[\s]([A-Z][\.])[\s]([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)",x)    
    #matches with middle name
    matches = re.findall("([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)[\s]([A-Z][a-z]+)[\s]([A-Z][a-z]+[-]?[A-Z]?[a-z]+[']?[s]?)",x)
    
    #matches = re.findall("[\s][a-z]+[\s]([A-Z][a-z|-]+[A-Z]?[a-z]+)[!\.,;\?][\s]",x) #gets all single capitalized words before a punctuation mark and a space -> but doesnt get words preceded by quotess

    
    
    print matches
    numbnames={}
    for name in matches:
        if name in numbnames:
            numbnames[name]+=1
        else:
            numbnames[name]=1
    
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
