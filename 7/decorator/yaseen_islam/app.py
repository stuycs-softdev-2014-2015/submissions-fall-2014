from flask import Flask, render_template, redirect, request, abort, jsonify, session, make_response, url_for

app = Flask(__name__)
app.secret_key = 'My name is Yaseen'


def auth(func):
    def wrapper():
        if "user" in session:
            return func()
        else:
            return redirect(url_for("login", redir=request.endpoint))
    return wrapper
            
@app.route('/logout')
def logout():
    if "user" in session:
        session.pop("user")
    return redirect('/login')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods=["POST","GET"])
def login(redir="home", *args, **kwargs):
    if request.method=="GET":
        return render_template('login.html')
    else:
        user=request.form["user"]
        passwd=request.form["passwd"]
        if user=="admin" and passwd=="masterpasswd":
            session["user"]=user
        return redirect(url_for(redir))

@app.route('/content')
@auth
def content():
    return render_template('content.html')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


            
