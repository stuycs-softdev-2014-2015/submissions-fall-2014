from flask import Flask, render_template, url_for, redirect, request, session
from functools import wraps

app = Flask(__name__)
app.secret_key = '32131231231231;(*@#$@)'

def get_form_value(key):
    return request.form[key].encode('ascii', 'ignore')

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session and session['username'] != None:
            return func()
else:
    return redirect(url_for('login'))
return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session and session['username'] != None:
        return redirect(url_for('home'))
    else:
        error = None
username = session['username']
if request.method == 'POST':
    username = get_form_value('username')
    password = get_form_value('password')
    if True:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        error = 'Incorrect username or password.'
return render_template('login.html', title='Login', error=error, username=username)

@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('login'))

@app.route('/')
@auth
def home():
    return render_template('home.html', title='home')

@app.route('/page')
@auth
def page():
    return render_template('page.html', title='Page')

if __name__ == '__main__':
    app.jinja_env.line_statement_prefix = '='
    app.debug = True
    app.run(host='0.0.0.0')
