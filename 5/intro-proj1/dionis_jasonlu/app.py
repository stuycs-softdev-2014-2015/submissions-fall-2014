from flask import Flask,render_template


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor

app = Flask(__name__)
@app.route("/Analysis")
@app.route("/Analysis", methods = ['Post'])
def Analysis():
    return render_template("Analysis.html")
@app.route("/Data")
@app.route("/Data", methods = ['Post'])
def data():
    return render_template("Data.html")

@app.route("/home")
@app.route("/home", methods = ['Post'])
@app.route("/Index")
@app.route("/")
def home():
    return render_template("Index.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8888)
