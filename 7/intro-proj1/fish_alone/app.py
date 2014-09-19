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
    if button==None:
        return render_template("choose.html")
    else:
        return render_template("chosen_pokemon.html", chosen=chosen_pokemon, name=uname)

@app.route("/chosen_pokemon")
def chosen_pokemon(chosen=None, name="Stupid Idiot who did not enter his/her name"):
    return render_template("chosen_pokemon.html",chosen=chosen, name=name)


if __name__=="__main__":
    app.debug = True
    app.run()
