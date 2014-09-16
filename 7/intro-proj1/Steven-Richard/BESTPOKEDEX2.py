def abilitycheck():
    data=open("Abilities").readlines()
    result=[]
    bigresult=[]
    tinyresult=""
    finder=0
    i=0
    for x in data:
        result.append(x[3:].strip().split("/t"))
    while i < len(result):
        tinyresult=result[i][0]
        while "\t" in tinyresult:
            if "*" in tinyresult:
                finder=tinyresult.find("*")
                tinyresult=tinyresult[:finder]+tinyresult[finder+1:]
            finder=tinyresult.find("\t")
            tinyresult=tinyresult[:finder]+","+tinyresult[finder+1:]
        bigresult.append(tinyresult)
        i+=1
    result=[]
    for x in bigresult:
        result.append(x.split(","))
    d={}
    for x in result:
        d[x[0]]=x[1:]
    return d
abilitydictionary=abilitycheck()

def countabilities():
    data= abilitydictionary.values()
    d={}
    for x in data:
        for y in x:
            if y not in d:
                d[y]=1
            else:
                d[y]+=1
    d.pop("")p
    return d
counts=countabilities()
