import login
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import Connection

app = Flask(__name__)
app.secret_key = "894984ntn8942hg9349gh4" #don't look at this it's secret

registrationError = "Error: this username already exists."
loginError = "Error: username of password incorrect."
authenticationError = "Error: you must be logged in to view this page."

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        button = request.form['submit']
        username = request.form['un']
        password = request.form['pw']
        if button == 'Register':
            tryReg = login.addUser(username, password)
            if tryReg:
                return redirect('/u/'+username)
            else:
                flash(registrationError)
                render_template("login.html")
        elif button == 'Login':
            tryLogin = login.login(username, password)
            if tryLogin:
                return redirect('/u/'+username)
            else:
                flash(loginError)
                render_template("login.html")
    return render_template("login.html")

@app.route('/u/<username>', methods=['GET', 'POST'])
def user(username=None):
    if request.method == 'POST':
        if request.form['logout'] == 'Logout':
            login.logout(username)
            return redirect(url_for('home'))
    if login.authenticated(username)== True:
        return render_template("user.html", username=username)
    else:
        flash(authenticationError)
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)
