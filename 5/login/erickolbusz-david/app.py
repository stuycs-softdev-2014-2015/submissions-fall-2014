from flask import Flask, render_template, request, redirect, session
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
    if ('username' in session):
        flash ("You are already logged in")
        redirect ("/welcome")
    user = request.args.get("username")
    pw = request.args.get("password")
    submit = request.args.get("submit")
    if (submit == "Submit"):
        res = db.authenticate(username,password)
        if (res == 1):
            user_list = db.users.find({'name':username, 'pw':password})
            user = user_list[0]
            new_login_count = user['logincount'] + 1
            users.update({'name':username, 'pw':password, 'logincount':new_login_count, 'info':user['info']}, upsert=True)
            session ['username'] = username
            session ['logins'] = new_login_count
            return redirect("/welcome")
        flash ("Invalid Username or Password")
    return render_template ("login.html")
    

@app.route("/register")
def register():
    if ('username' in session):
        flash ("You are already logged in")
        redirect ("/welcome")
    user = request.args.get("username","None")
    pw = request.args.get("password","None")
    register = request.args.get("register")
    if (register == "Register"):
        does_account_exist = db.authenticate(username)
        if (does_account_exist == 1):
            flash("Account already exists") #tried registering with taken username (None, None) is not a valid user/pass combo
        elif (len(username)<6):
            flash("Username too short, must be at least 6 characters") #username too short, None falls under here too
        elif (len(password)<8):
            flash("Password too short, must be at least 8 characters") #password too short, None falls under here too
        else:
            db.users.insert({'name':username,'pw':password,'logincount':1,'info':""})
            flash("Successfully registered")
    return render_template ("register.html") #have a button that redirects to /
    
@app.route("/welcome")
def welcome():
  return render_template ("welcome.html", username = session.get('username'), counter = session.get('logins')) #button for /about and for /logout
                      
@app.route ("/about")
def about():
  if (submit == "Submit"):
    user_list = db.users.find({'name':session.get("username")})
    user = user_list[0]
    info = user['info']
    addedinfo = request.args.get("userinfo")
    new_info = info + addedinfo
    users.update({'name':username, 'pw':password, 'logincount':new_login_count, 'info':new_info}, upsert=True)
  return render_template ("about.html", username = session.get("username"), userinfo = mongo.user_info(session.get("username")))

@app.route("/logout")
def logout():
  session.pop('username', None)
  session.pop('logins', None)
  flash('You were logged out')
  return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
