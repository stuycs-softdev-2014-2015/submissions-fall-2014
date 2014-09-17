from flask import Flask, render_template

app= Flask(__name__)

stream=open('scores.csv', 'r')
readas=stream.read()
stream.close()

@app.route("/data")
def data():
    ret = readas.splitlines()
    listolists= []
    for x in ret:
        innerlist = x.split(",")
        listolists.append(innerlist)
    return render_template("data.html",listolists=listolists)

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

if __name__=="__main__":
    app.debug = True
    app.run()
