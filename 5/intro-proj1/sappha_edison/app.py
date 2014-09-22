from flask import Flask, render_template,request

app = Flask (__name__)



@app.route ("/",methods=["GET","POST"])
def home ():
    data = open ("pokemon2.csv", "r")
    categories = data.read().splitlines()
    pokelist=[]
    results=[]
    for each in categories:
        pokeLine=each.split(",")
        pokelist.append(pokeLine)
    if request.method=="GET":
        return render_template("data.html",pokelist=pokelist)
    else:
        search = request.form["fname"]
        pokesearch=[]
        for each in categories:
            pokeLine=each.split(",")
            if pokeLine[0]==search:
                pokesearch.append(pokeLine)
        return render_template("data.html",pokesearch=pokesearch,pokelist=pokelist)

def index(match):
    if request.method == "POST":
        searched = request.form["fname"]
        if match == searched:
            return True
        else:
            return False

@app.route("/about")
def about():
    return render_template("about.html")

def enterWeb(filename, fill):
    with open("templates/" + filename, "wt") as change:
        with open("templates/data.html", "rt") as fwrite:
            for line in fwrite:
                change.write(line.replace("changeHere", fill))
    return


if __name__ == "__main__":
    app.debug = True
    app.run()
