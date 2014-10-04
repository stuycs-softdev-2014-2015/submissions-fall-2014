import re

comwords = ["My","We","You","He","She","Her","His","Mr","Mrs","Ms","Dr","The","Then","After","Before","Later","Next","Never","Perhaps","During","While","So","No","Not","Yes","But","To","Do","For","From","Who","What","When","Where","Why","How","Would","Was","Had","With","Their","They","There","This","That","Those","These","Well","By","On","At","As","An","Of","It","Is","If","In","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","January","February","March","July","August","September","October","November","December"]

def findNames(f):
    file = open(f, "r")
    file = file.read()
    print file

    #Find all words with capitalized first letters
    firstrun = re.findall(r'([A-Z][a-z]+)',file,re.S)

    #Put all words in a dictionary with the frequency of which they appear
    #If the word appears in the list of common words, do not add it
    secrun = {}
    for n in firstrun:
        if (n not in comwords):
            if (n not in secrun):
                secrun[n] = 1
            else:
                secrun[n]+=1

    #Reverse names and frequency for next step
    #looks like -> {1:"Yesterday, That", 100:"It", 124: "The", ...}
    names = {}
    for k,v in secrun.items():
        if (v not in names):
            names[v] = [k]
        else:
            names[v].append(k);

    #Takes out the least common words found 
    #(so sentence starters or uncommon names are removed)
    size = len(names)*4/5
    i = 0
    while( len(names) > size ):
        if i in names:
            del names[i]
        i += 1
    #print names

    #This just puts all the names in a final list
    namesfinal = []
    for l in names.values():
        for n in l:
            namesfinal.append(n)
    print namesfinal

findNames("TheLonelyUnicorn.txt")
