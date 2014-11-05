from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
import mongo

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template("home.html", username = session['username']);
    return render_template("index.html");

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        flash("You are already logged in. Please logout first.")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        r = mongo.addNewUser(request.form['username'], request.form['password'], 0)
        if (r[0]):
            flash("You successfully registered. You can now login.")
            return redirect(url_for("login"))
        else:
            flash(r[1])
    return render_template("register.html") #Happens if register unsuccessful

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash("You are already logged in. Please logout first.")
        return redirect("/")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        r = mongo.loginUser(request.form['username'], request.form['password'])
        print(r)
        if (r[0]):
            session['username'] = request.form['username']
            flash("You were successfully logged in")
            return redirect("/")
        else:
            flash(r[1])
    return render_template("login.html") #Happens if login unsuccessful

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out")
    return redirect("/")

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.debug=True
    app.run(host="0.0.0.0", port=5678)
