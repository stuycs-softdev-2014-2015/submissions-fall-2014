from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("Blank.html")

@app.route('/data')
def data():
    pokemon = {}
    f = open('pokemon.csv' ,'r')
    g = f.readlines()
    l = g[0].split(',')
    f.close()
    for x in g[1:]:
        r = x.split(',')
        pokemon[r[2].split(' ')[0]] = [int(r[3]),int(r[4]),int(r[5]),r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16]]
    name = request.args.get('name',None)
    if name == None or name not in pokemon.keys():
        return render_template("home.html", dataList = pokemon)
    else:
        return render_template("specific.html",n = name, dataLine = pokemon[name],l = l)

if __name__ == "__main__":
    app.run(debug='True')
