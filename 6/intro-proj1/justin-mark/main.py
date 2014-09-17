from flask import Flask, render_template
from data import read_attendance_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data")
def data():
    data = read_attendance_data()
    data.pop(0)
    return render_template("data.html", d={"data": data})


if __name__ == "__main__":
    app.debug = True
    app.run()
