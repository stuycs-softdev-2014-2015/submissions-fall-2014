#!/usr/bin/python

def pokedexreader():
    '''
    reads the source code of a bulbapedia to extract data
    '''
    sourcecodedata=open("Pokedex").readlines()
    codedata=[]
    pokemondata=[]
    pokedexnumber=0
    pokedexname=""
    onedigitcase=""
    for x in sourcecodedata:
        if '<span class="plainlinks"><a href="/wiki/' in x:
            pokedexnumber=x.find("title") + 7
            pokemondata += [x[pokedexnumber:pokedexnumber+3]]
            pokedexname=x.find("_")
            pokemondata += [x[45:pokedexname]]
        if '<td style="background:#' in x:
            onedigitcase= x[-4:-1].split()
            if onedigitcase[0]==">":
                pokemondata += x[-3:-1].split()
            else:
                pokemondata += x[-4:-1].split()
        if "</td></tr>" in x:
            codedata.append(pokemondata)
            pokemondata=[]
    return codedata
pokedexreader=pokedexreader()

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

def tableabilities():
    print "<A HREF='http://149.89.150.100/~richard.zhan/BESTPOKEDEXalpha.py'>Percents</a>"
    print "<A HREF='http://149.89.150.100/~richard.zhan/BESTPOKEDEXbeta.py'>Stats and Moves</a>"
    print "<table border=1>"
    print "<tr><td>Pokemon<td>Primary Ability<td>Secondary Ability<td>Dream World Ability"
    i=0
    a=0
    while i < len(pokedexreader):
        print "<tr><td>",pokedexreader[i][1]
        for x in abilitydictionary[pokedexreader[i][1]]:
            print "<td>", x
        i+=1
    print "</table>"
print "Content-type: text/html"
print
print "<pre>"
tableabilities()
print "</pre>"
