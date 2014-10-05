import re

comwords = open("filter.txt", "r").read().split("\n")

def namefilter(names):
    for x in names:
        if (x[0] in comwords or x[1] in comwords):
            x[0], x[1] = x[1], ''
    return [x for x in names if x != ['','']]

        
def findNames(f):
    filestream = open(f, "r")
    file = filestream.read()
    filestream.close()

    #Find all words with capitalized first letters and followed by another captitalized word, optional
    #result is returned into tuple form
    firstrun = re.findall(r"([A-Z][a-z\-]+)( [A-Z][a-zA-Z\-]+)?",file,re.S)
    #Filtering from list and covert the tuples into lists. and then conc together
    firstrun = namefilter([list(x) for x in firstrun])
    firstrun = [(x[0] + x[1] if x[1] != None else x[0]) for x in firstrun]

    #Put all words in a dictionary with the frequency of which they appear
    #If the word appears in the list of common words, do not add it
    secrun = {}
    for n in firstrun:
        if (n not in secrun):
            secrun[n] = 1
        else:
            secrun[n] += 1

    #Reverse names and frequency for next step
    #looks like -> {1:"Yesterday, That", 100:"It", 124: "The", ...}
    names = {}
    for k,v in secrun.items():
        if (v not in names):
            names[v] = [k]
        else:
            names[v].append(k)
    size = len(names)*4/5
    i = 0
    while( len(names) > size ):
        if i in names:
            del names[i]
        i += 1

    #This just puts all the names in a final list
    namesfinal = []
    for l in names.values():
        for n in l:
            namesfinal.append(n)
    print namesfinal

if __name__ == "__main__":
    findNames("TheLonelyUnicorn.txt")
