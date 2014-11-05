
from flask import Flask,request,redirect,render_template,session
from pymongo import Connection,MongoClient



################################ mongo stuff ############################
conn=Connection()
db = conn['portas-troiae']
#collection = db['user-info']

def add(username,password):
    #adds to the database
    db.users.insert( {'name': username, 'password': password} )
    print "addded"

def check(username, password):
    #makes sure the username and password are valid
    thing = capere("name", username, "name")
    print thing
    if thing != None:
        #this user already exists
        return False
    if len(password) < 4:
        #password is too short
        return False
    else:
        return True



#helper function to get stuff from database:
def capere (field, data, want):
  thing = None
  for post in db.users.find( {field:data} ):
    thing = post[want]
  return thing


def authenticate (username, password):
    verusPass = capere("name", username, "password")
    if verusPass == password:
      return True
    else:
      return False







################################ webapp stuff ###########################

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def base():
    #print authenticate("rebecca", "benedict")
    #print authenticate("rebecca", "yuste")
    #print check("b", "doctor")
    #Yes this is a copy of user, but at 4:38 the time is already wasted and we will clean the code later today and for later incarnations
    print "logging" in session
    if "logged" not in session:
      session['logged'] = False
    if "logging" in session:
      logging = session["logging"]
      print logging
      session.pop("logging", None)
      if logging:
        return render_template("home.html", logging = logging, logged = session['logged'])
      else:
        return render_template("login.html", logging = logging, logged = session['logged'])
    if "success" in session:
      success = session["success"]
      session.pop("success", None)
      if success:
        return render_template("login.html", success = success, logged = session['logged'])
      else:
        return render_template("register.html", success = success, logged = session['logged'])
    return render_template("login.html", logged = session['logged'])

@app.route("/register", methods=["GET", 'POST'])
def register():
  if "logging" in session:
    logging = session["logging"]
    print logging
    session.pop("logging", None)
    if logging:
      return render_template("home.html", logging = logging, logged = session['logged'])
    else:
      return render_template("login.html", logging = logging, logged = session['logged'])
  if "success" in session:
    success = session["success"]
    session.pop("success", None)
    if success:
      return render_template("login.html", success = success, logged = session['logged'])
    else:
      return render_template("register.html", success = success, logged = session['logged'])
  return render_template("register.html", logged = session['logged'])

@app.route("/logging", methods=['POST'])
def index():
    print "logging"
    if request.method=='POST':
        #get info in login fields, verify it
        #if it works -> send to caligula ;)
        #if not -> back to login.html with error message
        username=request.form["username"]
        password=request.form["password"]
    if authenticate(username, password):
      if "user" not in session:
        session['user'] = username
      session['logging'] = True
      session['logged'] = True
      return redirect("/home")
    else:
      session['logging'] = False
      return redirect("/")

#A moment of silence for our fallen code :|
'''@app.route("/cladius")
def test():
  if 'user' in session:
    return render_template("cladius.html")
  else:
    return render_template('fail.html')'''

@app.route("/registering", methods= ['POST'])
def regis():
    if request.method=='POST':
        #get the info from the fields
        #some verification (don't overlap with any name already in the databass
        #put into the database
        username =request.form['username']
        password=request.form['password']
    if check(username, password):
      add(username,password)
      session["success"] = True
      print session['logged']
      return redirect("/")
    else:
      session["success"] = False
      return redirect("/")


@app.route("/logout")
def logout():
    #remove session
    #return base (with message)
    session.clear()
    session['logged'] = False
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html", logged = session['logged'])

#Ruuun Trees Ruuunnnn, the logging is coming!!!
@app.route("/home")
def home():
  if "logging" in session:
    logging = session["logging"]
    session.pop("logging", None)
    if logging:
      return render_template("home.html", logging = logging, logged = session['logged'])
    else:
      return render_template("login.html", logging = logging, logged = session['logged'])
  return render_template("home.html", logged=session["logged"])
@app.route("/caesar")
def hail():
    if 'user' in session:
        return render_template("caesar.html", logged = session['logged'])
    else:
        return redirect("/")

@app.route("/dogs")
def omfg():
    if 'user' in session:
        return render_template("dogs.html", logged = session['logged'])
    else:
        return redirect("/")

@app.route("/caligula")
def caligula():
    if 'user' in session:
        return render_template("caligula.html", logged = session['logged'])
    else:
        return redirect("/")
@app.route("/bees")
def bees():
    if 'user' in session:
        return render_template("bees.html", logged = session['logged'])
    else:
        return redirect("/")

if __name__=="__main__":
    app.secret_key="Its still a project so to Github this shall go"
    app.debug=True
    app.run()
