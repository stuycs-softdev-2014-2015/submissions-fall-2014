from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    r = "<h1>Welcome to the league of desu</h1>"
    r += '<a href="/desu">desu</a>'
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

if __name__ == "__main__":
    app.debug = True
    app.run()
