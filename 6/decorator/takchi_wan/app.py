from flask import Flask
from flask import render_template, session, redirect, request
from functools import wraps

app = Flask (__name__)
app.secret_key = "emorybound"

@app.route('/')
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
            return index('You've logged in.')
        else:
            return index('Incorrect credentials. Please try again.')
            
            
if __name__ == "__main__":
	app.run(debug = True)
