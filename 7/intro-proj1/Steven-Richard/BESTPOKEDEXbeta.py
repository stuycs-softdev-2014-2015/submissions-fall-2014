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
    for y in pokedexreader:
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
        pokedexmod.append(x+sum+[sum[0]/6]+[movesdictionary[x[1]]])
    return pokedexmod
pokedexmod=pokedexmod()

def tablestuff():
    print "<A HREF='http://149.89.150.100/~richard.zhan/BESTPOKEDEXalpha.py'>Percents</a>"
    print "<A HREF='http://149.89.150.100/~richard.zhan/BESTPOKEDEXtheta.py'>Abilities</a>"
    print "<table border=1>"
    print "<tr><td>#<td>Pokemon<td>HP<td>ATK<td>DEF<td>Sp.ATK<td>Sp.DEF<td>SPEE<td>BST<td>AVG<td>Viable Moves"
    i=0
    a=0
    while i < len(pokedexmod):
        print "<tr>"
        while a < len(pokedexmod[i]):
            print "<td>",pokedexmod[i][a]
            a+=1
        a=0
        i+=1
    print "</table>"
print "Content-type: text/html"
print
print "<pre>"
tablestuff()
print "</pre>"


