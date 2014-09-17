from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/choose")
def choose():
    return render_template("choose.html")

#@app.route("/squirtle")
#@app.route("/bulbasaur")
#@app.route("/charmander")
#def home():
#    return render_template("pokemon_page.html",name=name)

if __name__=="__main__":
    app.debug = True
    app.run()
