from flask import Flask, render_template,session,redirect, request
import mongodb_helper

app=Flask(__name__)

@app.route("/")
def index():
    if 'SESS_ID' not in session:
        # default value for now
        session['SESS_ID']=0
        
    sess_id = session['SESS_ID']
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if (insert(username, password)):
        return redirect("/")
    return render_template("register.html")

@app.route("/logout", methods=['POST'])
def logout():
    session.pop('n',None)
    return redirect("/")

@app.route("/home")
def home():
    return render_template("home.html",username)

@app.route("/info")
def info():
    return render_template("info.html",username)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.debug=True
    app.secret_key="this key shouldn't be on github"
    app.run(host="0.0.0.0",port=1119)
