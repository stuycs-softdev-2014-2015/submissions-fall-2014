from flask import Flask, render_template, session, redirect, request, flash, escape
import userdb_helper

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # need some validation here
        if 'username' in session and userdb_helper.user_exists(session['username']):
            return redirect("/home")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (userdb_helper.validate_login(username, password)):
            session['username'] = request.form['username']
            return redirect("/home")
        else:
            flash("Login error: Incorrect username or password.")
    return render_template("index.html", page_title="Home")
        

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        if(password == password2):
            result = userdb_helper.validate(username, password)
            if (not result[0]): # invalid username or password 
                flash(result[1])
                return render_template("register.html", page_title="Register")
            result = userdb_helper.insert(username, password)
            if (result[0]): # valid registration
                flash(result[1])
                return redirect("/")
            else: # user already exists
                flash(result[1])
                return render_template("register.html", page_title="Register")
        else:
            flash("Registration error: Passwords do not match.")
            return render_template("register.html", page_title="Register")

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username',None)
    flash("Successfully logged out.")
    return redirect("/")

@app.route("/home")
def home():
    if('username'in session):
        return render_template("home.html", page_title="Home", username=escape(session['username']))
    else:
        return redirect("/")

@app.route("/info")
def info():
    try:
        username=escape(session['username'])
    except:
        return redirect("/")
    return render_template("info.html", page_title="Info", username=escape(session['username']), info=userdb_helper.getInfo(escape(session['username'])))

@app.route("/update", methods=['GET','POST'])
def update():
    try:
        username=escape(session['username'])
    except:
        return redirect("/")
    if request.method == 'GET':
        return render_template("update.html", page_title="Update Info",username=escape(session['username']))
    else:
        name = request.form['name']
        job = request.form['job']
        age = request.form['age']
        print age
        result = userdb_helper.updateInfo(username,name,job,age)
        flash(result)
        return render_template("update.html", page_title="Update Info",username=escape(session['username']))

@app.route("/about")
def about():
    return render_template("about.html", page_title="About")

if __name__=="__main__":
    app.debug=True
    app.secret_key="this key shouldn't be on github"
    app.run(host="0.0.0.0",port=1119)
