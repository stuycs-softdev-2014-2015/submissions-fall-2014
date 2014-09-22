from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("login.html")
    else:
        
        uname = request.form['user']
        pword = request.form['password']
        
        valid = (uname == "stuycs" and pword == "softdev")
        if  (valid):
            return render_template("Analysis1.html")
        else:
            return render_template("login.html")

if __name__ =="__main__":
    app.debug = True
    app.run()
