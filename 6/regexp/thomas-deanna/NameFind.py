import re 

def FindNames():

    #getting possible names from string
    file = open('Bible.txt')
    regex=re.compile("[A-Z][a-z]+[^0-9][^\W][\s]")
    names = regex.findall(file.read())
    file.close()

    #cross referencing with list of popular names
    file = open('popnames.txt')
    regex2=re.compile("[A-Z]+")
    popnames  = regex2.findall(file.read())
    """print len(names)"""
    file.close()

    #Testing where we lose names
    print len(names)

    for n in range(len(popnames)):
        popnames[n] = popnames[n].lower().capitalize()
    i = 0
    print len(names)

    while i < len(names):
        if not names[i] in popnames:
            names.remove(names[i])
        else:
            i+= 1

    #cross referencing with a dictionary
    file = open('dictionary.txt')
    regex3 = re.compile("[a-z]+")
    dictWords = regex3.findall(file.read())
    file.close()
    for n in range(len(dictWords)):
        dictWords[n] = dictWords[n].lower().capitalize()
    i=0
    while i < len(names):
        if names[i] in dictWords:
            names.remove(names[i])
        else:
            i+=1

    #print
    """print popnames"""
    print len(names)
    print names

        
if __name__ == "__main__":
    FindNames()

    
