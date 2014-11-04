from flask import Flask, render_template, request, redirect, session
import mongo

app = Flask(__name__)
id=0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

#login page
@app.route("/")
def index():
    user = request.args.get("username","None")
    pw = request.args.get("password","None")
    if (user == "None" and pw == "None"):
      return render_template ("login.html") #have a button that redirects to /register
    if mongo.login(user,pw):
      session ['username'] = username
      return redirect("/welcome")
    

@app.route("/register")
def register():
    user = request.args.get("username","None")
    pw = request.args.get("password","None")
    register = request.args.get("register")
    if (submit == "Register")
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
    sumSessionCounter();
    return render_template ("welcome.html", username = session.get("username"), l, counter = session.get ("counter")) #button for other page (?) and for /logout
                      
@app.route('/logout')
def logout():
  session.pop('username', None)
  flash('You were logged out')
  return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
