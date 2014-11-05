from flask import Flask, render_template, request

app = Flask(__name__)

def tabledata():
    f = open('wastecollection.csv', 'r')
    s = f.readlines()
    f.close
    finals = []
    i = 0
    while i < len(s):
        s[i] = s[i].split(',')
        finals.append(s[i])
        i += 1
    return s

@app.route("/")
def analysis():
    return render_template("analysis.html", table = tabledata())
@app.route("/analysis")
def analysis():
    return render_template("analysis.html", table = tabledata())
@app.route("/data")
def data():
    return render_template("page.html", table = tabledata())
@app.route("/compare", methods=["GET","POST"])
def compare():
    boroughdistricts = []
    for district in tabledata()[1:]:
        boroughdistricts.append(district[1] + district[2])
    if(request.args.get("table") == None):
        return render_template("compare.html", table = boroughdistricts)
    else:
        return render_template("compare.html", tabledata = tabledata(), table = boroughdistricts, districts_selected = request.args.getlist("table"))
if __name__ == "__main__":
    app.debug = True
    app.run()
