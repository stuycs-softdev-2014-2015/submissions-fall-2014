from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        button = request.form['b']
        uname = request.form['uname']
        pword = request.form['pword']
        name = request.form['name']
        valid = (uname == "stuycs" and pword == "softdev")
        if button=="cancel":
            return render_template("form.html")
        elif not (valid):
            return render_template("form.html",helper="yes")
        else:
            return render_template("page.html", name=name)


@app.route("/page")
@app.route("/page/<name>")
def page(name=None):
    return render_template("page.html", name=name)


if __name__ =="__main__":
    app.debug = True
    app.run()
