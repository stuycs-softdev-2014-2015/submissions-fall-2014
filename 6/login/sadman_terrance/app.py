from flask import Flask, render_template, request
import csv
import pymongo

conn = pymongo.MongoClient()
db = conn.sadterry
accounts = db.accounts

app = Flask(__name__) 



@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
   if request.method=='POST':
      print '\nThe request method is ' + str(request.method) + '\n' 
      
      username = request.form['username']
      password = request.form['password']
      #print user + " : " + password;
      print 'Username and Password have been recorded as variables'
      
      #db.drop_collection('accounts')
      doc = {"username":username, "password":password}
      
      #db.accounts.insert(doc);
      #print db.accounts.find() + '\n'
      exists = False
      loggedin = False
      incorrectlogin = False
      
      for d in db.accounts.find():
         if username == d['username']:
            exists = True
            savedpass = d['password']
            
      if (exists == True and savedpass == password):
         loggedin = True

      if (exists == True and savedpass != password):
         incorrectlogin = True
         
      for d in db.accounts.find():
         print d['username']
         print d['password']
         
      #print db.accounts.find({username:'a', password:"a"})  
      doc = list(db.accounts.find({})) 
      #print doc
      #print conn.database_names()
      print ''
      print db.collection_names()
      print db
      print ''
      
      print "login status"
      print incorrectlogin
      return render_template("login.html", exists=exists, loggedin=loggedin, username=username, password=password, incorrectlogin=incorrectlogin)
   else:
      return render_template("login.html", loggedin=False)
  
@app.route("/logout")
def logout():
   pass
   #logout

@app.route("/register",methods=['GET','POST'])
def register():
   pass
   #register

@app.route("/intro")
def intro():
   pass
   #can view without logging in

@app.route("/funny")
def funny():
   pass
   #viewed only if logged in

@app.route("/joke")
def joke():
   pass
   #viewed only if logged in

if __name__ == "__main__":
   app.debug = True
   app.run()
