def csvtolist(csvname):
    csvtable = []
    csvf = open(csvname)
    csvln = csvf.readlines()
    csvf.close()
    for ln in csvln:
        csvtable.append(ln.strip().split(","))
    return csvtable

def getcol(table,col):
    r = []
    for ln in table:
        r.append(ln[col])
    return r

def killcol(table,col):
    for ln in table:
        del ln[col]

def makestatdict(champnames):
    r = {}
    for name in champnames:
        r[name] = {}
    return r

def addstatnames(statdict,statnamelist):
    for champ in statdict.keys():
        for stat in statnamelist:
            statdict[champ][stat] = "PLACEHOLDER"

def populatestatdict(statdict,stattable):
    statnames = stattable[0]
    nameindex = statnames.index("Name")
    for ln in stattable[1:]:
        name = ln[nameindex]
        for i in range(len(statnames)):
            statdict[name][statnames[i]] = ln[i]

def init():
    global statdict
    global champnames
    global statnames
    stattable = csvtolist("data/stats.csv")
    wrtable = csvtolist("data/winrate.csv")
    killcol(wrtable,0)

    statnames = stattable[0]+wrtable[0][1:]
    champnames = getcol(stattable[1:],1)
    statdict = makestatdict(champnames)

    addstatnames(statdict,stattable[0])
    addstatnames(statdict,wrtable[0])

    populatestatdict(statdict,stattable)
    populatestatdict(statdict,wrtable)

################

init()

#print champnames
#print statnames
#print statdict
