from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World</h1>"

@app.route("/page")
@app.route("/page/<name>")
def page(name=None):
    return render_template("page.html", name=name)

if __name__ =="__main__":
    app.debug = True
    app.run()
