from flask import Flask, render_template, session, redirect, request, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'edricsha'

def auth(func):
    @wraps(func)
    def inner():
        if 'user' in session:
            return func()
        else:
            return redirect(url_for('login'))
    return inner
        
@app.route('/')
@auth
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form["username"]
        pw = request.form["password"]
        if user == "foo" and pw == "goo":
            session['user'] = user
        return redirect('/')

@app.route('/logout')
@auth
def logout():
    session.pop('user')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
