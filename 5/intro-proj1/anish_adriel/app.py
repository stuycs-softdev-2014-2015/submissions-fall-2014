from flask import Flask,render_template
# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result/")
@app.route("/result/<Type>")
def result(Type=None):
    return render_template("result.html",Type=Type)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6734)
