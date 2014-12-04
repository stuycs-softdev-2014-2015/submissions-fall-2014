import re

#this was to test. Ignore this
#with open ("PrideandPrej.txt", "r") as myfile:
#    data=myfile.read().replace('\n', '')

def findName(s):
    f = "((([A-Z][a-z]+)|M([rs]|rs)\.)( [A-Z][a-z]+)+)"
    res = re.findall(f, s)
    L = []
    for k in res:
        L.append(k[0])
    return L

def cleanAndTallyNames(L):
    res = {}
    s = ""
    for k in L:
        ##if "Ms. " in k or "Mr. " in k:
        ##    s = k[3:]
        ##else:
        s = k
        if s not in res:
            res[s] = 0
        i = res[s]
        i = i + 1
        res[s] = i
    winner = ""
    num = 0
    for n in res:
        if res[n] > num:
            winner = n
            num = res[n]
    return winner


def findDate(s):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthsAbbrv= []
    L = []

    for i in months:
        monthsAbbrv.append(i[:3])
    f1 = "(\d{1,2})[,.-/](\d{1,2})[,.-/]((\d\d){1,2})"
    res1 = re.findall(f1,s)
    for g in res1:
        H = [int(g[0]), int(g[1])]
        if int(g[2]) < 100:
            H.append(int(g[2]) + 1900)
        else:
            H.append(int(g[2]))
    L.append(H)

    for k in range(0,12):
        f2=  months[k] + " (\d{1,2}), ((\d\d){1,2})"
        res2 = re.findall(f2,s)
        for g in res2:
            H = [k+1, int(g[0])]
            if int(g[1]) < 100:
                H.append(int(g[1]) + 1900)
            else:
                H.append(int(g[1]))
            L.append(H)
        f2=  monthsAbbrv[k] + "\.* (\d{1,2}), ((\d\d){1,2})"
        res2 = re.findall(f2,s)
        for g in res2:
            H = [k+1, int(g[0])]
            if int(g[1]) < 100:
                H.append(int(g[1]) + 1900)
            else:
                H.append(int(g[1]))
            L.append(H)
        f3= "(\d{1,2}) (" + months[k] + "||" + ") (\d{4})"
        res3 = re.findall(f3,s)
        for g in res3:
            H = [k+1, int(g[0]), int(g[2])]
            L.append(H)
    return L

def cleanAndTallyDates(L):
    res = {}
    for k in L:
        s = str(L[0]) + "-" + str(L[1]) + "-" + str(L[2])
        if s not in res:
            res[s] = 0
        i = res[s]
        i = i + 1
        res[s] = i
    winner = ""
    num = 0
    for n in res:
        if res[n] > num:
            winner = n
            num = res[n]
    return winner

#only run these
#data should be a list of strings
def processNames(data):
    L = []
    for i in data:
        g = findName(i)
        L.extend(g)
    return cleanAndTallyNames(L)
def processDates(data):
    L = []
    for i in data:
        g = findDate(i)
        L.extend(g)
    return cleanAndTallyDates(L)
