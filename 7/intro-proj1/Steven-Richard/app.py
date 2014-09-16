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

@app.route("/home")
def home():
    return render_template("home.html",codedata = pokedexreader());
    
if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()
