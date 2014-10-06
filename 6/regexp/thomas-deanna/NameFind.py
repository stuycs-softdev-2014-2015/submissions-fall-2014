import re 

def FindNames():

    #getting possible names from string
    with open('Charlie.txt', "r") as myfile:
        book=myfile.read().replace('\n', '')

    regex = "[A-Z][a-z]+[^0-9][^\W][\s]"
    ProperNames = re.findall(regex, book)

    #cross referencing with list of popular names
    with open('popnames.txt', 'r') as myfile:
        listnames=myfile.read().replace('\n', '')

    regex2= "[A-Z]+"
    popnames = re.findall(regex2, listnames)

    for n in range(len(popnames)):
        popnames[n] = popnames[n].lower().capitalize()
    
    final=[]
    i = 0

    for n in popnames:
        if n in ProperNames:
            final.append(n)

            """
    while i < len(ProperNames):
        if ProperNames[i] in popnames:
            final.append(ProperNames[i])
            i+=1
        else:
            i+=1
   
    #cross referencing with a dictionary
    file = open('dictionary.txt')
    regex3 = re.compile("[a-z]+")
    dictWords = regex3.findall(file.read())
    file.close()
    for n in range(len(dictWords)):
        dictWords[n] = dictWords[n].lower().capitalize()
    i=0
    while i < len(ProperNames):
        if ProperNames[i] not in dictWords:
            final.append(ProperNames[i])
            i+=1
        else:
            i+=1
    """
    
    #print

    print ProperNames
    print final
        
if __name__ == "__main__":
    FindNames()

    
