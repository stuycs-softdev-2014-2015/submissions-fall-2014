from flask import Flask, render_template, request
import coder

app = Flask (__name__)

@app.route ("/")
def home () :
    return render_template ("index.html")

@app.route ("/table")
def table ():
    s = "<table>"
    data = open ("Lincoln_Square_BID_Business_List.csv", "r")
    t = data.readline().split(',')
    for b in t:
        s = s + "<th>" + b + "</th>"
    data.readline()
    for line in data:
        s = s + "<tr>"
        t = line.split(',')
        for b in t:
            s = s + "<td>" + b + "</td>"
        s = s + "</tr>"
    data.close()
    s = s + "</table>"
    replacer("table.html", s)
    return render_template("table.html")

@app.route("/input")
def input ():
    input = request.args.get ("input", None)
    button = request.args.get ("button", None)
    if button == None:
        return render_template ("input.html")
    elif button == "Codify!":
        return render_template("results.html")%coder.codify(input)
    elif button == "Decodify!":
        return render_template("results.html")%coder.decodify(input)

@app.route("/about")
def about():
    replacer("about.html", "<p>This is really just us messing around with css and tables, honestly.</p>")
    return render_template("about.html")

def replacer(filename, replaceWith):
    with open("templates/" + filename, "wt") as fout:
        with open("templates/data.html", "rt") as fin:
            for line in fin:
                fout.write(line.replace("---REPLACE---", replaceWith))
    return


if __name__ == "__main__":
    app.debug = True
    app.run()
