#! /usr/bin/python
from flask import Flask
from flask import render_template

app = Flask(__name__)

data = open("data.txt", 'r').read().split("\n")

import cgi
@app.route("/" methods= ["GET", "POST"])
def mainpage():
    search = request.args.get("id",None)
    return render_template("Pokemon.html", search=search)
    

@app.route("/<int:pokemonid>")
def search(pokemonid):
    source = data[pokemonid].split(",")
    pid = source[0]
    name = source[1]
    hp = source[2]
    atk = source[3]
    defs = source[4]
    satk = source[5]
    sdef = source[6]
    spd = source[7]
    ttl = source[8]
    return render_template("id.html", pid=pid, name=name, hp = hp, atk=atk, defs=defs , satk=satk , sdef=sdef , spd=spd , ttl=ttl)

if __name__ == "__main__":
    app.run(debug=True)
