#! /usr/bin/python
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

data = open("data.txt", 'r').read().decode('utf-8').split("\n")
x = 0
while x < len(data):
    data[x] = data[x].split(",")
    x += 1

@app.route("/")
def mainpage():
    return render_template("Pokemon.html", data=data)

@app.route('/', methods=['POST'])
def redirect():
    searchid = request.form['text']
    return redirect(url_for('psearch', pokemonid=searchid), code=302)

@app.route("/search/<int:pokemonid>")
def psearch(pokemonid):
    source = data[pokemonid]
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
