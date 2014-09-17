from flask import Flask, render_template

# app is an instance of the Flask class
app = Flask(__name__)

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

#pokedexreader=pokedexreader();

def pokemovesdictionary():
    '''
    Creates a dictionary of viable moves for the pokemon
    '''
    d={}
    datas=open("Viable Moves").readlines()
    data=[]
    do=False
    i=0
    p=pokedexreader()
    for x in datas:
        data.append(x.strip().split())
    for y in p:
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


@app.route("/home")
def home():
    return render_template("home.html",
                           codedata=pokedexreader(),
                           movesdictionary = pokemovesdictionary())
    
if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()
