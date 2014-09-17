from flask import Flask, render_template
from data import read_attendance_data, sort_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data")
def data():
<<<<<<< HEAD
    y =  l
    return render_template("data.html", d={"data":y})
    

f='School_Attendance_and_Enrollment_Statistics_by_District__2010-11_.csv'


def open_file(filename):
    L=[]
    for line in open(filename).readlines():
        L.append (line.strip().split(","))
    return L
l = open_file(f)
l.pop(0)

def findMax (l):
    new = []
    for i in l:
        new.append(int(i[2]))
    new.pop(len(new) -1)
    return max(new)

def findMin(l):
    new = []
    for i in l:
        new.append(int(i[2]))
    new.pop(len(new) -1)
    new.pop(len(new) -1)
    return min(new)
def findMaxPercent(l):
    new = []
    for i in l:
        new.append(i[1])
    new.pop(len(new) -1)
    new.pop(len(new) -1)
    return max(new)

def findMinPercent(l):
    new = []
    for i in l:
        new.append(i[1])
    new.pop(len(new) -1)
    new.pop(len(new) -1)
    return min(new)
=======
    data = read_attendance_data()
    data.pop(0)
    return render_template("data.html", d={"data": data})
>>>>>>> e1ee24d3228d5ee67d6fa03f2bd0a697de8ee84b

@app.route("/facts")    
def facts():
    x = findMax(l) 
    y = findMin(l)
    z = findMaxPercent(l)
    a = findMinPercent(l)
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
