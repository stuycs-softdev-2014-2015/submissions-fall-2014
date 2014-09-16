from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World</h1>"

@app.route("/page")
def page():
    return render_template("page.html")

if __name__ =="__main__":
    app.debug = True
    app.run()
