from flask import Flask, render_template

app = Flask (__name__)

@app.route ("/")
def home ():
    s = "<center><table border = '1' width = '91%' style='background-color: rgb(230,230,250)'>"
    data = open ("pokemon2.csv", "r")
    categories = data.readline().split(',')
    for each in categories:
        s = s + "<th>" + each + "</th>"
    data.readline()
    for line in data:
        s = s + "<tr>"
        categories = line.split(',')
        for each in categories:
            s = s + "<td width = '10%'><center><font color='blue'>" + each + "</font></center></td>"
        s = s + "</tr>"
    data.close()
    s = s + "</table><center>"
    enterWeb("home.html", s)
    return render_template("home.html")

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
