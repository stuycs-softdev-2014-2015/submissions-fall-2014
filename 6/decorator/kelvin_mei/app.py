from flask import Flask
from flask import render_template, redirect, url_for, session, request
from functools import wraps

app = Flask(__name__)
app.secret_key = 'key'

def auth(x):
    @wraps (x)
    def wrapper (*args, **kwds):
        if not 'user' in session:
            return redirect ('/')
        return x(*args, **kwds)
    return wrapper

@app.route ('/', methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template ('login.html')
    else:
        usern = request.form['username'].encode('ascii','ignore')
        passw = request.form['password'].encode('ascii','ignore')
        if usern == 'Zamansky' and passw == 'SoftDev':
            session['user'] = 'Zamansky'
            return redirect ('/Success')
        else:
            return redirect ('/')

@app.route('/Success')
@auth
def work():
    if request.method == "POST":
        return redirect ('/logout')
    return render_template("success.html")

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect ('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
