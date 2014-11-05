from flask import Flask
from flask import render_template, session, redirect, request, url_for
from functools import wraps

app = Flask (__name__)
app.secret_key = "emorybound"

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func()
        else:
            return redirect(url_for('login'))
    return wrapper
        
@app.route('/')
@auth
def index():
    return render_template('index.html')
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "abc" and password == "123":
            session['username'] = username
            return render_template("index.html")
        else:
            return render_template("login.html")
            
@app.route('/test')
@auth
def testpage():
    return render_template('test.html')
            
@app.route('/logout')
def logout():
	session.pop("username")
	return redirect(url_for('login'))
	
if __name__ == "__main__":
	app.run(debug = True)
	
