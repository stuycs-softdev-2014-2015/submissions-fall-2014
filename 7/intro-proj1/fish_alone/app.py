from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/choose")
def choose():
    button = request.args.get("b",None)
    chosen_pokemon = request.args.get("pokemon",None)
    if button==None:
        return render_template("choose.html")
    else:
        return render_template("home.html")#will change!

#@app.route("/squirtle")
#@app.route("/bulbasaur")
#@app.route("/charmander")
#def home():
#    return render_template("pokemon_page.html",name=name)

if __name__=="__main__":
    app.debug = True
    app.run()
