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
#[[#,Name,HP,ATK,DEF,SP.ATK,SP.DEF,SPE],[

def pokedexmod():
    '''
    Includes the BST and the AVG stats
    '''
    pokedexmod=[]
    for x in pokedexreader:
        sum=[int(x[2])\
                          +int(x[3])\
                          +int(x[4])\
                          +int(x[5])\
                          +int(x[6])\
                          +int(x[7])]
        pokedexmod.append(x+sum+[sum[0]/6])
    return pokedexmod
pokedexmod=pokedexmod()
#[[#,Name,HP,ATK,DEF,SP.ATK,SP.DEF,SPE,BST,AVG],[

def pokemovesdictionary():
    '''
    Creates a dictionary of viable moves for the pokemon
    '''
    d={}
    datas=open("Viable Moves").readlines()
    data=[]
    do=False
    i=0
    for x in datas:
        data.append(x.strip().split())
    for y in pokedexmod:
        while do == False and i<len(data):
            if [y[1].lower()+":", '{']==data[i]:
                finder = i
                do == True
            elif len(data[i]) > 2:
                if [y[1].lower()+":",'{'] == [data[i][0]+" "+data[i][1],'{']:
                    finder = i
                    do == True
            i+=1
        do = False
        d[y[1]]= data[finder+1][1][2:].split('":1,"')
        d[y[1]][-1]=d[y[1]][-1][:-5]
        d[y[1]]=" ".join(d[y[1]]).upper()
        finder = 0
        i=0
    return d
movesdictionary=pokemovesdictionary()

countingmoves=movesdictionary.values()
def countmoves():
    result=[]
    result2=[]
    for x in countingmoves:
        result.append(x.split(" "))
    for x in result:
        result2 += x
    d={}
    for x in result2:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    return result2

countmoves=countmoves()

def abilitycheck():
    data=open("Abilities").readlines()
    result=[]
    bigresult=[]
    tinyresult=""
    for x in data:
        result.append(x[3:].strip().split("/t"))
    for x in result:
        while "\t" not in x:
            x=x.replace("\t",",",3)
        
        

        
    
