from flask import Flask, render_template, request
from data import read_attendance_data, sort_data, find_facts

app = Flask(__name__)


@app.route("/")
def home():
    data = read_attendance_data()
    facts = find_facts(data)

    return render_template("home.html", d={"data": data, "facts": facts})


@app.route("/data", methods=["POST"])
def data():
    data = read_attendance_data()
    if request.method == "POST":
        data = read_attendance_data()
        print request.form
        data = sort_data(data, request.form['order'])

    return render_template("data.html", d={"data": data})


if __name__ == "__main__":
    app.debug = True
    app.run()
