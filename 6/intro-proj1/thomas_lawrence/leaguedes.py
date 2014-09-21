from flask import Flask,render_template,request
import utils
import data

data.statdict

app = Flask(__name__)

def csvtolist(csvname):
    csvtable = []
    csvf = open(csvname)
    csvln = csvf.readlines()
    csvf.close()
    for ln in csvln:
        csvtable.append(ln.split(","))
    return csvtable

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/desu")
def desu():
    return render_template("desu.html",
                           stattable=csvtolist("data/stats.csv"),
                           wrtable=csvtolist("data/winrate.csv"))

@app.route("/kun")
def kun():
    csvtable = csvtolist("data/stats.csv")
    return render_template("kun.html",
                           csvtable=csvtable,
                           columnstoget = [0,1,2,4,6,8,10,12,14,16,18,19])

@app.route("/form",methods=['GET','POST'])
def form():
    csvtable = csvtolist("data/stats.csv")
    if request.method=="GET":
        return render_template("form.html",
                               champnames=data.champnames)
    else:
        champs = request.form["champion"]
        action = request.form["a"]
        if action=="go":
            return render_template("generator.html",
                                   champs=champs,
                                   statnames=data.statnames,
                                   statdict=data.statdict)
        else :
            return render_template("home.html")
        


if __name__ == "__main__":
    app.debug = True
    app.run()
