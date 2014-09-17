from flask import Flask, render_template

#app is an instance of the Flask class
app = Flask(_name)

@app.route("/")
@app.route("/home")
def home():
    return render_template("Analysis_Final.html")


@app.route("/analysis")
def analysis():
    return render_template("Analysis_2.html")

if _name_ == "_main_":
    app.debug = True
    app.run()
