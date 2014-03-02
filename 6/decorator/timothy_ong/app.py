from flask import Flask, render_template,session,redirect,request

app = Flask(__name__)
app.secret_key = "asdf"

def auth(func):
    def wrapper(*args):
        if 'username' in session:
            return func()
        else:
            return index('you gotta log in buddy')
    return wrapper

@app.route('/')
def index(message = None):
    return render_template('index.html', message=message)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "asdf" and password == "asdf":
            session['username'] = username
            return index('success')
        else:
            return index('failure')

@app.route('/topsecret')
@auth
def topsecret():
    return render_template('topsecret.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return index()

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
