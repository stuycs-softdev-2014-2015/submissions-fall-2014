from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/miami")
def help1():
    return render_template("miami.html")

@app.route("/dallas")
def help2():
    return render_template("dallas.html")

@app.route("/la")
def help3():
    return render_template("la.html")

@app.route("/home")
def help4():
    return render_template("home.html")


@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index(name=None):
    if request.method ==  "GET":
        return render_template("index.html",name=None)
    else:
        user = request.form["user"]
        button = request.form["login"]
        if button==None :
            return render_template("index.html",name=None)
        else:
            return render_template("home.html",name=user)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=1061)
    
