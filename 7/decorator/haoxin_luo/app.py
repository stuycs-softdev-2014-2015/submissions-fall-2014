from flask import Flask,session,redirect,request,url_for,render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'blahb'


def auth(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not 'user' in session:
            return redirect(url_for('login',blah=request.endpoint))
        return func(*args,**kwargs)
    return wrapper

@app.route('/',methods=["GET","POST"])
@auth
def home():
    if request.method == "POST":
        return redirect(url_for('logout'))
    b = 'user' in session
    return render_template("index.html")

@app.route('/foo')
@auth
def foo():
    return "this is the foo page"

@app.route('/login/<blah>',methods=['GET',"POST"])
def login(blah):
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form['name']
        pw = request.form['pw']
        if user == 'admin' and pw == 'admin':
            session['user'] = 'admin'
            return redirect(url_for(blah))
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
