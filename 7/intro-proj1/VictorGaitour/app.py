from flask import Flask, render_template, request
import authenticate
# app is an instance of the Flask class
app = Flask(__name__)
//Idea for login-thingy from http://designscrazed.net/css-html-login-form-templates/
@app.route("/home",methods=["GET","POST"])
def home():
    errmess=""
    if request.method=="GET":
        return render_template("home.html",l=list)
    else:
        button = request.form['b']
        uname  = request.form['uname']
        pword  = request.form['pword']
        if button=="login":
            if authenticate.authenticate(uname,pword):
                return render_template("both.html")
            else :
                errmess= "Invalid Username and/or Password. Please try again."
                return render_template("home.html", errmess=errmess)
        if button=="cancel":
            return render_template("home.html")

@app.route("/zestats")
def zestats():
    return render_template("analysis.html")

@app.route("/data")
def data():
    return render_template("data.html")
@app.route("/help")
def help():
    return "<h1> LOL jk there is no help page</h1>"





if __name__=="__main__":
    # set the instance variable debug to True
    app.debug = True
    # call the run method
    app.run()
