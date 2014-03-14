
from flask import Flask
from flask import render_template, session, url_for, redirect, request
from functools import wraps


app = Flask(__name__)
app.secret_key = "Everything you know is wrong"


def auth(dec_arg):
    def outer(func):
        @wraps(func)
        def inner():
            if 'return_url' in session:
                return redirect(url_for(session.pop('return_url',None)))
            if 'username' in session:
                return func()
            session['return_url'] = dec_arg[1:]
            return redirect(url_for('login'))
        return inner
    return outer



@app.route("/index")
def index():
    session.clear()
    return render_template("index.html")



@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html",invalid="False")
    else:
        usernameu = request.form['username']
        username = usernameu.encode('ascii','ignore')
        passwordu = request.form['password']
        password = passwordu.encode('ascii','ignore')

    if username == 'user' and password == 'user':
        session['username'] = username
        return redirect(url_for('loggedin'))
    else:
        return render_template("login.html",invalid="True")



@app.route("/loggedin")
@auth("/loggedin")
def loggedin():
    return render_template("loggedin.html")

@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))



if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
