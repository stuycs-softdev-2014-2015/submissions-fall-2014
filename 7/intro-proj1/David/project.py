from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
@app.rout("/analysis")
@app.route("/data")
def data():
    return render_template("page.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
