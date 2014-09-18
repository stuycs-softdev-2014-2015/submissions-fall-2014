from flask import Flask, render_template, request
import authenticate

# app is an instance of the Flask class
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['b']
        global name
        name = request.form['name']
        password = request.form['password']
        if button=="Login":
            if authenticate.authentic(name, password):
                return render_template("data.html", name = name, dataList = dataHelper())
            else:
                return render_template("login.html")


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
