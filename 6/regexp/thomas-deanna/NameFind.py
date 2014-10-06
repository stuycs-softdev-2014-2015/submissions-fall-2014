import re 

def FindNames():

    #getting possible names from string
    with open('Charlie.txt', "r") as myfile:
        book=myfile.read().replace('\n', '')

    regex = "[A-Z][a-z]+[^0-9][^\W][\s]"

    """regex=re.compile("[A-Z][a-z]+[^0-9][^\W][\s]")
    names = regex.findall(file.read())
    file.close() """

    ProperNames = re.findall(regex, book)

    """
    #cross referencing with list of popular names
    file = open('popnames.txt')
    regex2=re.compile("[A-Z]+")
    popnames  = regex2.findall(file.read())
    print len(names)
    file.close()

    #Testing where we lose names
    print len(names)

    for n in range(len(popnames)):
        popnames[n] = popnames[n].lower().capitalize()
    i = 0
    print len(names)

<<<<<<< HEAD
    while i < len(names):
        if not names[i] in popnames:
            names.remove(names[i])
        else:
            i+= 1

    """

=======
    newNames = []
    for i in range(len(names)):
        if names[i] in popnames:
            newNames.append(names[i])
>>>>>>> 9d7a5119d0f178334a4481ef6020b2f1a7d5fca0
    #cross referencing with a dictionary
    file = open('dictionary.txt')
    regex3 = re.compile("[a-z]+")
    dictWords = regex3.findall(file.read())
    file.close()
    for n in range(len(dictWords)):
        dictWords[n] = dictWords[n].lower().capitalize()
<<<<<<< HEAD
    final=[]
    i=0
    while i < len(ProperNames):
        if ProperNames[i] not in dictWords:
            final.append(ProperNames[i])
            i+=1
    
    #print
    """
    print popnames
    print len(names)
    print names
    """
    print ProperNames
=======

    newNames2 = []
    for n in range(len(names)):
        if not names[n] in dictWords:
            newNames2.append(names[n])
    print newNames2
    #print
    """print popnames"""
    


>>>>>>> 9d7a5119d0f178334a4481ef6020b2f1a7d5fca0
        
if __name__ == "__main__":
    FindNames()

    
