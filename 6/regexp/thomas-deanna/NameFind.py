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

    #print
    """print popnames"""
    print len(names)
    print names

        
if __name__ == "__main__":
    FindNames()

    
