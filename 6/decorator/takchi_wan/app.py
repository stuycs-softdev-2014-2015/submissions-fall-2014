from flask import Flask
from flask import render_template, session, redirect, request
from functools import wraps

app = Flask (__name__)
app.secret_key = "emorybound"

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func()
        else:
            return index('Please log in first.')
        return wrapper
        
@app.route('/')
def index():
    return render_template('index.html', message=message)
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "abc" and password == "123":
            session['username'] = username
            return index('You have logged in.')
        else:
            return index('Incorrect credentials. Please try again.')
            
@app.route('/test')
@auth
def testpage():
    return render_template('test.html')
            
@app.route('/logout')
def logout():
	session.pop("username")
	return redirect(url_for('/'))
	


def testpage():
if __name__ == "__main__":
	app.run(debug = True)
