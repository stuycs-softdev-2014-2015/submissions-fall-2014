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

    newNames = []
    for i in range(len(names)):
        if names[i] in popnames:
            newNames.append(names[i])
    #cross referencing with a dictionary
    file = open('dictionary.txt')
    regex3 = re.compile("[a-z]+")
    dictWords = regex3.findall(file.read())
    file.close()
    for n in range(len(dictWords)):
        dictWords[n] = dictWords[n].lower().capitalize()

    newNames2 = []
    for n in range(len(names)):
        if not names[n] in dictWords:
            newNames2.append(names[n])
    print newNames2
    #print
    """print popnames"""
    


        
if __name__ == "__main__":
    FindNames()

    
