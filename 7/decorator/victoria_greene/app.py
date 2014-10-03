from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "this is a very secret key"

from functools import wraps
def auth(url):
    def wrapper(func):
        @wraps(func)
        def funkifier(*args, **kwargs):
            if 'username' in session:
                return func(*args, **kwargs)
            else:
                session['url'] = url
                return redirect('/login')
        return funkifier
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.form['username'] == 'user' and request.form['password'] == '123':
            session['username'] = request.form['username']
            if 'url' in session:
                return redirect(session['url'])
            else:
                return redirect('/')
        else:
            return render_template('login.html')

@app.route('/')
def home():
    return '<h1>Home page</h1><a href="/userstuff">this is protected stuff</a>'

@app.route('/userstuff')
@auth('/userstuff')
def protected_stuff():
    return '<h1>User Profile</h1> Top secret stuff up in here'

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')
