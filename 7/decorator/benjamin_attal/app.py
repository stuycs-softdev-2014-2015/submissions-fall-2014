from flask import Flask, render_template, session, redirect, request
from functools import wraps


app = Flask(__name__)
app.secret_key = 'dali_llama'


def auth(red_url, logged_in=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if logged_in:
                if 'user' in session:
                    return func(*args, **kwargs)
                else:
                    return redirect(red_url)
            else:
                if 'user' not in session:
                    return func(*args, **kwargs)
                else:
                    return redirect(red_url)

        return wrapper

    return decorator


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@auth('/')
def profile():
    return render_template('profile.html', user=session['user'])


@app.route('/login', methods=['GET', 'POST'])
@auth('/', logged_in=False)
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        session['user'] = request.form['user']
        return redirect('/')


@app.route('/logout')
@auth('/')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
