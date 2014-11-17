from flask import Flask, render_template, request, session
import csv
import pymongo
from functools import wraps

conn = pymongo.MongoClient()
db = conn.sadterry
accounts = db.accounts


app = Flask(__name__) 

#checks if logged in at each function call
def loggedin(func):
   @wraps(func)
   def inner():
      if 'username' in session:
         login=True
         user=session['username']
      else:
         login=False
         user='-'
      return func(login,user)
   return inner

@app.route("/")
@loggedin
def home(login,user):
   return render_template("base.html", loggedin=login, username=user)

@app.route("/login",methods=['GET','POST'])
@loggedin
def login(login,user):
   if login:
      return render_template("login.html", loggedin=True, username=user)

   if request.method=='POST':
      
      username = request.form['username']
      password = request.form['password']
      print 'Username and Password have been recorded as variables'
      
      exists = False
      loggedin = False
      reason = ""
     
      for d in db.accounts.find():
         if username == d['username']:
            exists = True
            savedpass = d['password']
      
      if exists == False:
         reason = "The username "+ username + " does not exists."
            
      if (exists == True and savedpass == password):
         loggedin = True

      if (exists == True and savedpass != password):
         reason = "Your username and password do not match"
         
         
      doc = list(db.accounts.find({})) 

      print ''
      print db.collection_names()
      print db
      print ''
 
      if loggedin:
         session['username']=username

      return render_template("login.html", loggedin=loggedin, username=username, reason=reason)
   else:
      print session
      return render_template("login.html", loggedin=False)
   #login
     
@app.route("/logout")
@loggedin
def logout(login,user):
   if login:
      session.pop('username', None)
      return render_template("logout.html", loggedin=False, previous=True)
   else:
      return render_template("logout.html",loggedin=False, previous=False)
   #logout

@app.route("/register",methods=['GET','POST'])
@loggedin
def register(login,user):
   if request.method=='POST':
      if 'username' not in session:
      
         username = request.form['username']
         password = request.form['password']
         reppassword = request.form['password2']
         
         reason = ""
         registered=False
         
         if password == reppassword:
            registered=True
         else:
            registered=False
            reason = "Passwords do not match"
            print "Passwords do not match"


         for d in db.accounts.find():
            if username == d['username']:
               registered=False
               reason="The username "+username+" already exists!"
               print "Username %s already in use" %username

         if registered:
            doc = {"username":username, "password":password}
            db.accounts.insert(doc)
            print 'Username and Password have been recorded as variables'
         else:
            print "Failure to register"
         
         if registered:
            return render_template("register.html", page=1, username=username)
      return render_template("register.html", page=2, reason=reason)
   else:
      return render_template("register.html", page=3, loggedin=login, username=user) 
   #register

@app.route("/funny")
@loggedin
def funny(login,user):
   return render_template("funny.html", loggedin=login, username=user) 
   #viewed only if logged in

@app.route("/joke")
@loggedin
def joke(login,user):
   return render_template("joke.html", loggedin=login, username=user) 
   #viewed only if logged in

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "Sadman<3Terrance"
   app.run()
