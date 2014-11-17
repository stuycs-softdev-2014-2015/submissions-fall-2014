from flask import Flask, render_template, request, session
import csv
import pymongo

conn = pymongo.MongoClient()
db = conn.sadterry
accounts = db.accounts


app = Flask(__name__) 



@app.route("/")
def home():
   if 'username' in session:
      loggedin=True
      username=session['username']
   else:
      loggedin=False
      username = '-'
   print loggedin
   return render_template("base.html", loggedin=loggedin, username=username)

@app.route("/login",methods=['GET','POST'])
def login():
   if 'username' in session:
      luser = session['username']
      return render_template("login.html", loggedin=True, username=luser)

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
def logout():
   if 'username' in session:
      session.pop('username', None)
      print "login status: logged in"
      return render_template("logout.html", loggedin=False, previous=True)
   else:
      print "login status: not logged in"
      return render_template("logout.html",loggedin=False, previous=False)
   #logout

@app.route("/register",methods=['GET','POST'])
def register():
   if 'username' in session:
      loggedin=True
      username=session['username']
   else:
      loggedin=False
      username=''

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
      return render_template("register.html", page=3, loggedin=loggedin, username=username) 
   #register

@app.route("/funny")
def funny():
   if 'username' in session:
      loggedin=True
      username=session['username']
   else:
      loggedin=False
      username=''
   return render_template("funny.html", loggedin=loggedin, username=username) 

   #viewed only if logged in

@app.route("/joke")
def joke():
   if 'username' in session:
      loggedin=True
      username=session['username']
   else:
      loggedin=False
      username=''
   return render_template("joke.html", loggedin=loggedin, username=username) 

   #viewed only if logged in

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "Sadman<3Terrance"
   app.run()
