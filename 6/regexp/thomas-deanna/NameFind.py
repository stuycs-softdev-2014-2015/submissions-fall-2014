import re 

def FindNames():

    #getting possible names from string
    file = open('names.txt')
    regex=re.compile("[A-Z][a-z]+[^0-9][^\W][\s]")
    names = regex.findall(file.read())
    file.close()

    #cross referencing with list of popular names
    file = open('popnames.txt')
    regex2=re.compile("[A-Z]+")
    popnames  = regex2.findall(file.read())
    print len(popnames)
    file.close()
    for n in range(len(popnames)):
        popnames[n] = popnames[n].lower().capitalize()
    final = []
    for i in range(len(names)):
        if names[i] in popnames:
            final.append(names[i])
    #print
    print final
    
        
if __name__ == "__main__":
    FindNames()

    
