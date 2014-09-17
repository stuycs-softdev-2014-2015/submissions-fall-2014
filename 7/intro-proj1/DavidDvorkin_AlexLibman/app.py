from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Blank.html")

@app.route('/data')
def data():
    pokemon = {}
    f = open('pokemon.csv','r')
    g = f.readlines()[1:]
    f.close()
    for x in g:
        r = x.split(',')
        pokemon[r[1]] = [r[2],r[3],r[4],r[5],r[6],r[7],r[8]] #Change around which data values to use (arbitrarily chosen at the moment)
    return send_file("pokemon.csv") ,render_template("home.html", dataList = pokemon) #Data inputted into templated as dataList
if __name__ == "__main__":
    app.run(debug='True')
