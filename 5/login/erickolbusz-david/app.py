from flask import Flask, render_template, request, redirect, session
import mongo

app = Flask(__name__)
id=0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#login page
@app.route("/")
def index():
    if (session.get('username') != "")
        flash ("You are already logged in")
        redirect ("/welcome")
    session ['username'] = ""
    user = request.args.get("username")
    pw = request.args.get("password")
    submit = request.args.get("submit")
    if (submit == "Submit"):
      if mongo.login(user,pw):
        session ['username'] = username
        return redirect("/welcome")
      else:
        flash ("Invalid User or Password")
    return render_template ("login.html")
    

@app.route("/register")
def register():
    if (session['username'] != "")
        flash ("You are already logged in")
        redirect ("/welcome")
    user = request.args.get("username","None")
    pw = request.args.get("password","None")
    register = request.args.get("register")
    if (register == "Register"):
        error = mongo.add_account(user,pw)
        if (error == 0):
            flash("Successfully registered")
            return redirect ("/")
        if (error == 1):
            flash("Account already exists")
        if (error == 2):
            flash("Username too short, must be at least 6 characters")
        else:
            #error = 3
            flash("Password too short, must be at least 8 characters")
    #flash the message
    return render_template ("register.html") #have a button that redirects to /
    
@app.route("/welcome")
def welcome():
  return render_template ("welcome.html", username = session.get('username'), counter = mongo.login_count(session.get('username'))) #button for other page (?) and for /logout
                      
@app.route ("/about")
def about():
  if (submit == "Submit"):
    userinfo = request.args.get('userinfo')
    mongo.change_info(session.get('username'), userinfo)
  return render_template ("about.html", username = session.get('username'), userinfo = mongo.user_info(session.get('username')))

@app.route("/logout")
def logout():
  session.pop('username', None)
  flash('You were logged out')
  return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
