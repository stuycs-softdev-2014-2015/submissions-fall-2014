from flask import Flask, render_template, request, redirect, session, flash, url_for
from pymongo import Connection

app = Flask(__name__)
id=0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

conn = Connection()
db = conn['accountinfo']
users = db.users

#login page
@app.route("/")
def index():
    if ('username' not in session):
        session ['username'] = None
        session ['currentp'] = "login"
    if (session.get('username') != None):
        flash ("You are already logged in!")
        if (session.get('currentp') == "about"):
            user_list = db.users.find({'name':session.get("username")})
            user = user_list [0]
            info = user['info']
            redirect ("/about")
            return render_template ("about.html", username = session.get("username"), userinfo = info)
        else:
            redirect ("/welcome")
            return render_template ("welcome.html", username = session.get('username'), counter = session.get('logins'))
    session ['username'] = None
    session ['currentp'] = "login"
    username = request.args.get("username")
    password = request.args.get("password")
    submit = request.args.get("submit")
    if (submit == "Submit"):
        i = users.find({'name':username, 'pw':password}).count()
        print i
        does_account_exist = (users.find({'name':username, 'pw':password}).count() == 1)
        if (does_account_exist == True):
            user_list = db.users.find({'name':username, 'pw':password})
            user = user_list[0]
            new_login_count = user['logincount'] + 1
            users.update({'name':username}, {"$set": {'logincount':new_login_count}})
            session ['username'] = username
            session ['logins'] = new_login_count
            return redirect("/welcome")
        flash ("Invalid Username or Password")
    return render_template ("login.html")
    

@app.route("/register")
def register():
    if (session.get('username') != None):
        flash ("You are already logged in!")
        if (session.get('currentp') == "about"):
            redirect ("/about")
            user_list = db.users.find({'name':session.get("username")})
            user = user_list [0]
            info = user['info']
            return render_template ("about.html", username = session.get("username"), userinfo = info)
        else:
            redirect ("/welcome")
            return render_template ("welcome.html", username = session.get('username'), counter = session.get('logins'))
    session ['currentp'] = "register"
    username = request.args.get("username")
    password = request.args.get("password")
    register = request.args.get("register")
    if (register == "Register"):
        does_account_exist = (users.find({'name':username}).count() > 0)
        if (does_account_exist == True):
            flash("Account already exists") #tried registering with taken username (None, None) is not a valid user/pass combo
        elif (len(username)<6):
            flash("Username too short, must be at least 6 characters") #username too short, None falls under here too
        elif (len(password)<8):
            flash("Password too short, must be at least 8 characters") #password too short, None falls under here too
        else:
            db.users.insert({'name':username,'pw':password,'logincount':0,'info':""})
            flash("Successfully registered")
            redirect("/")
            return render_template ("login.html")
    return render_template ("register.html") #have a button that redirects to /
    
@app.route("/welcome")
def welcome():
    if (session.get('username') == None):
        flash ("You are not logged in!")
        if (session.get('currentp') == "login"):
            redirect ("/")
            return render_template ("login.html")
        else:
            redirect ("/register")
            return render_template ("register.html")
    session ['currentp'] = "welcome"
    return render_template ("welcome.html", username = session.get('username'), counter = session.get('logins')) #button for /about and for /logout
                      
@app.route ("/about")
def about():
    if (session.get('username') == None):
        flash ("You are not logged in!")
        if (session.get('currentp') == "login"):
            redirect ("/")
            return render_template ("login.html")
        else:
            redirect ("/register")
            return render_template ("register.html")
    session ['currentp'] = "about"
    submit = request.args.get("submit")
    user_list = db.users.find({'name':session.get("username")})
    user = user_list[0]
    info = user['info']
    if (submit == "Submit"):
        addedinfo = request.args.get("userinfo")
        new_info = info + addedinfo + " : " 
        users.update({'name':session.get("username")}, {"$set": {'info':new_info}}) 
        info = new_info
    return render_template ("about.html", username = session.get("username"), userinfo = info)

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('logins', None)
    session.pop('currentp', None)
    session ['currentp'] = "login"
    flash('You are or were already logged out')
    return redirect("/")

@app.route ("/aboutproj")
def aboutproj():
    return render_template ("aboutproject.html")

@app.route ("/random")
def random():
    return render_template ("random.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
