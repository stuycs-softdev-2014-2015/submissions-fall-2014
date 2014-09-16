from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/data")
def data():
    l = open_file(f)
    l.pop(0)
    return render_template("data.html", d={"data":l})
    

f='School_Attendance_and_Enrollment_Statistics_by_District__2010-11_.csv'


def open_file(filename):
    L=[]
    for line in open(filename).readlines():
        L.append (line.strip().split(","))
    return L


if __name__ == "__main__":
    app.debug = True
    app.run()
