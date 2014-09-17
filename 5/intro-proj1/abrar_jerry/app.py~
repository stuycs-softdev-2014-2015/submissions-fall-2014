from flask import Flask, render_template

app = Flask(__name__)

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/page1")
def help():
    return "<h2>Hello2<h2>"

@app.route("/home")
@app.route("/")
def home():
   return "<h1>Hello</h1>"


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=1061)
    
