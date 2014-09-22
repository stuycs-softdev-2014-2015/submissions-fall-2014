from flask import Flask,render_template,request
import utils
import data

app = Flask(__name__)

def csvtolist(csvname):
    csvtable = []
    csvf = open(csvname)
    csvln = csvf.readlines()
    csvf.close()
    for ln in csvln:
        csvtable.append(ln.strip().split(","))
    return csvtable

def csvtodict(csvname):
    csvdict = {}
    csvf = open(csvname)
    csvln = csvf.readlines()
    csvf.close()
    for ln in csvln:
        pair = ln.split(",")
        csvdict[pair[0]] = pair[1]
    return csvdict

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/all")
def desu():
    return render_template("desu.html",
                           stattable=csvtolist("data/stats.csv"),
                           wrtable=csvtolist("data/winrate.csv"))

@app.route("/level")
def kun():
    csvtable = csvtolist("data/stats.csv")
    return render_template("kun.html",
                           csvtable=csvtable,
                           columnstoget = [0,1,2,4,6,8,10,12,14,16,18,19])

@app.route("/form",methods=['GET','POST'])
def form():
    selects=10 #number of dropdowns on form.html
    
    if request.method=="GET":
        statcbformat = csvtolist("data/statcheckboxformat.csv")
        statglossary = csvtodict("data/statglossary.csv")
        return render_template("form.html",
                               champnames=data.champnames,
                               statnames=data.statnames,
                               selects=selects,
                               statcbformat=statcbformat,
                               statglossary=statglossary)
    else:
        champs = []
        for i in range(selects):
            curchamp = request.form["champ"+str(i)]
            if curchamp!="":
                champs.append(curchamp)
        action = request.form["a"]
        lookupstats = request.form.getlist("lookupstats")
        if action=="Compare":
            return render_template("generator.html",
                                   champs=champs,
                                   lookupstats=lookupstats,
                                   statnames=data.statnames,
                                   statdict=data.statdict)
        else :
            return render_template("home.html")
        


if __name__ == "__main__":
    app.debug = True
    app.run()
