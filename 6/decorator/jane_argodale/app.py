from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)
app.secret_key = 'jane'

def auth(func):
    def wrapper(*args,**kwargs):
        if 'username' in session:
            return func()
        else:
            return redirect(url_for("login"))
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username'] #no db, will take any username/pw
        password = request.form['password']
        session['username'] = username
    return redirect("/")

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect("/login")

@app.route('/')
@auth
def home():
    return render_template("home.html",username=session['username'])

if __name__ == "__main__":
    app.run(debug = True)
