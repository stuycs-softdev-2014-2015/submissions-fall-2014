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
    uname = request.args.get("uname",None)
    if button==None or (button!=None and chosen_pokemon==None):
        return render_template("choose.html")
    else:
        if (chosen_pokemon=="bulbasaur"):
            return bulbasaur(uname)
        elif (chosen_pokemon=="charmander"):
            return charmander(uname)
        else:
            return squirtle(uname)

@app.route("/bulbasaur")
def bulbasaur(name="some generic name"):
    return render_template("bulbasaur.html", name=name)

@app.route("/charmander")
def charmander(name="some generic name"):
    return render_template("charmander.html", name=name)

@app.route("/squirtle")
def squirtle(name="some generic name"):
    return render_template("squirtle.html", name=name)


if __name__=="__main__":
    app.debug = True
    app.run()
