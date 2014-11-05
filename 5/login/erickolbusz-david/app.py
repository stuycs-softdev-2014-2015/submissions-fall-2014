from flask import Flask, render_template, request, redirect, session, flash
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
    if (session.get('username') != None):
        flash ("You are already logged in!")
        redirect ("/welcome")
    session ['username'] = None
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
        redirect ("/welcome")
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
    return render_template ("register.html") #have a button that redirects to /
    
@app.route("/welcome")
def welcome():
    if (session.get('username') == None):
        flash ("You are not logged in!")
        redirect ("/")
    return render_template ("welcome.html", username = session.get('username'), counter = session.get('logins')) #button for /about and for /logout
                      
@app.route ("/about")
def about():
    if (session.get('username') == None):
        flash ("You are not logged in!")
        redirect ("/")
    submit = request.args.get("submit")
    user_list = db.users.find({'name':session.get("username")})
    user = user_list[0]
    info = user['info']
    if (submit == "Submit"):
        addedinfo = request.args.get("userinfo")
        new_info = info + addedinfo + "<br>" + "\n"
        users.update({'name':session.get("username")}, {"$set": {'info':new_info}}) 
    info = user['info']
    return render_template ("about.html", username = session.get("username"), userinfo = info)

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('logins', None)
    flash('You were logged out')
    return redirect("/")

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
