from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    r = '''<body background="static/leaguebackground.jpg">'''
    r += "<h1>Welcome to the league of desu</h1>"
    r += '<a href="/desu">desu</a>'
    r += '<br><a href="/kun">kun</a></body>'
    return r

@app.route("/desu")
def desu():
    csvtable = []
    csvf = open("data/out.csv")
    csvln = csvf.readlines()
    csvf.close()
    for ln in csvln:
        csvtable.append(ln.split(","))
    return render_template("desu.html",
                           csvtable=csvtable)

@app.route("/kun")
def kun():
    csvtable = []
    csvf = open("data/out.csv")
    csvln = csvf.readlines()
    csvf.close()
    for ln in csvln:
        csvtable.append(ln.split(","))
        return render_template("kun.html",csvtable=csvtable,columnstoget = [0,1,2,4,6,8,10,12,14,16,18,19])


if __name__ == "__main__":
    app.debug = True
    app.run()
