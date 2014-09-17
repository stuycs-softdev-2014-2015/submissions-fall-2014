from flask import Flask,render_template


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/Source")
def about():
    return render_template("Source.html")

@app.route("/Analysis")
def Analysis():
    return render_template("Analysis.html")
@app.route("/Data")
def data():
    return render_template("Data.html")

@app.route("/home")
@app.route("/Index")
@app.route("/")
def home():
    return render_template("Index.html")

if __name__=="__main__":
    app.debug=True
    app.run()
    #app.run(host="0.0.0.0",port=8888)
