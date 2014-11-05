from flask import Flask, render_template, request, redirect
import authenticate

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    message = ""
    if request.method=="GET":
        return render_template("login.html", message = message)
    else:
        button = request.form['b']
        print button
        global name
        name = request.form['name']
        password = request.form['password']
        if button=="Login":
            if authenticate.authentic(name, password):
                return render_template("data.html", name = name, dataList = dataHelper())
            else:
                message = "Username and password did not match our records. Please try again."
                return render_template("login.html", message = message)


@app.route("/stuycs")
def stuycs():
    return redirect("http://www.stuycs.org")

@app.route("/enschool")
def enschool():
    return redirect("http://stuy.enschool.org/")

@app.route("/tools")
def tools():
    return redirect("https://students-stuyhs.theschoolsystem.net/login.rb")

@app.route("/google")
def google():
    return redirect("http://www.google.com")

@app.route("/facebook")
def facebook():
    return redirect("http://www.facebook.com")

@app.route("/whitehouse")
def whitehouse():
    return redirect("http://www.whitehouse.gov")


def dataHelper():
    f = open('data/data.csv', 'r')
    dataList = [];
    line = f.readline()
    while line:
        tmpList = []

        for i in line.split(','):
            tmpList.append(str(i))

        dataList.append(tmpList)
        line = f.readline()
    f.close()
    return dataList


@app.route("/data")
def data():
    return render_template("data.html", dataList = dataHelper(), name = name)



def analysisHelper():
    t = open('data/data2.csv', 'r')
    analysisList = [];
    line = t.readline()
    while line:
        tmpList = []

        for i in line.split(','):
            tmpList.append(str(i))

        analysisList.append(tmpList)
        line = t.readline()
    t.close()
    return analysisList

@app.route("/analysis")
def analysis():
    return render_template("analysis.html", analysisList = analysisHelper())


if __name__ == "__main__":
    app.run(debug=True)
