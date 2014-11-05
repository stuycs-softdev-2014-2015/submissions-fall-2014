
from flask import Flask,request,redirect,render_template,session
from pymongo import Connection,MongoClient


#Sorry Mr.Z
global LoginButtonPressed = False
global RegisterButtonPressed = False

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

@app.route("/")
def base():
    #print authenticate("rebecca", "benedict")
    #print authenticate("rebecca", "yuste")
    #print check("b", "doctor")
    if "logging" in session:
      if session["logging"]:
        return render_template("home.html", logging = session["logging"])
      else:
        return render_template("login.html", logging = session["logging"])
    if "success" in session:
      if session["success"]:
        return render_template("login.html", success = session["success"])
      else:
        return render_template("login.html", success = session['success'])
    return render_template("login.html")

@app.route("/logging", methods=['POST'])
def index():
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
      return redirect("/")
    else:
      session['logging'] = False
      return redirect("/")

@app.route("/cladius")
def test():
  if 'user' in session:
    return render_template("cladius.html")
  else:
    return render_template('fail.html')

@app.route("/registering")
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
      return redirect("/")
    else:
      session["success"] = True
      return redirect("/")
      

@app.route("/logout")
def logout():
    #remove session
    #return base (with message)
    session.pop('n',None)
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home") 
def home():
    if 'user' in session:
        return render_template("home.html")
    else:
        return redirect("/")

@app.route("/caesar")
def hail():
    if 'user' in session:
        return render_template("caesar.html")
    else:
        return redirect("/")

@app.route("/dogs")
def omfg():
    if 'user' in session:
        return render_template("dogs.html")
    else:
        return redirect("/")

@app.route("/caligula")
def caligula():
    if 'user' in session:
        return render_template("caligula.html")
    else:
        return redirect("/")
@app.route("/bees")
def bees():
    if 'user' in session:
        return render_template("bees.html")
    else:
        return redirect("/")

if __name__=="__main__":
    app.secret_key="Don't put this on github"
    app.debug=True
    app.run()
