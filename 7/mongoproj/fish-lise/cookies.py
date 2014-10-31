from flask import Flask,render_template,request, redirect,session
import utils

app=Flask(__name__)
        
@app.route("/")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("index.html")
    else:
        u = request.form['uname']
        pswd = request.form['pswd']
        valid_user = utils.authenticate(u,pswd)
        if not(valid_user):
            return render_template("index.html",l=l)
        else:
            session['myuser'] = u
            
            return render_template("index.html",
                                   name=uname)

@app.route("/register")
def register():
        ru = request.form['runame']
        rpswd = request.form['rpswd']
        if adduser(ru,rpswd):
                return render_template("index.html", rconf = "You have successfully registered.")
        else:
                return render_template("register.html", rconf="Username taken. Try Again.")
        
@app.route("/logout")
def logout():
    return "<h1>This is the logout page</h1>"
@app.route("/info")
def info():
    return "<h1>This is the info page</h1>"

@app.route("/loggedin1")
def loggedin1():
    return "<h1>This is the first logged in page</h1>"

@app.route("/loggedin2")
def loggedin2():
    return "<h1>This is the second logged in page</h1>"

if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=5000)
