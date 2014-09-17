from flask import Flask, render_template
from data import read_attendance_data, sort_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data")
def data():
    data = read_attendance_data()
    data.pop(0)

    return render_template("data.html", d={"data": data})


def findMax(l):
    new = []
    for i in l:
        new.append(int(i[2]))
    new.pop(len(new) - 1)
    return max(new)


def findMin(l):
    new = []
    for i in l:
        new.append(int(i[2]))
    new.pop(len(new) - 1)
    new.pop(len(new) - 1)
    return min(new)


def findMaxPercent(l):
    new = []
    for i in l:
        new.append(i[1])
    new.pop(len(new) - 1)
    new.pop(len(new) - 1)
    return max(new)


def findMinPercent(l):
    new = []
    for i in l:
        new.append(i[1])
    new.pop(len(new) - 1)
    new.pop(len(new) - 1)
    return min(new)
    data = read_attendance_data()
    data.pop(0)
    return render_template("data.html", d={"data": data})


@app.route("/facts")
def facts():
    data = read_attendance_data()
    data.pop(0)

    x = findMax(data)
    y = findMin(data)
    z = findMaxPercent(data)
    a = findMinPercent(data)
    return render_template("facts.html",x=x, y=y,z=z, a=a)


@app.route("/data/<order>")
def data_order(order="attendance-desc"):
    data = read_attendance_data()
    data.pop(0)

    if order:
        sort_data(data, order)

    return render_template("data.html", d={"data": data})

if __name__ == "__main__":
    app.debug = True
    app.run()
