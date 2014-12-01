from flask import Flask, flash, render_template, request, redirect, session
import db

app = Flask(__name__)
app.secret_key = "MTYIXatgAP2y6fIvq8MrAN8RKgHg2B8p"

#HOME:
@app.route("/")
def home():
   if request.method == "GET":
      if "user" in session:
         return render_template("home.html", status="Log out")
      else:
         return render_template("home.html", status="Log in")
   else:
      if "user" not in session:
         return redirect("/login")
      else:
         return redirect("/logout")

#ABOUT:
@app.route("/about", methods=['GET', 'POST'])
def about():
   if request.method == "GET":
      return render_template("about.html")
   else:
      return redirect("/login")

#LOGIN:
@app.route("/login", methods=['GET', 'POST'])
def login():

   if "user" not in session:
        if request.method == "GET":
           return render_template("login.html")
        else:
            user = request.form['username']
            pwrd = request.form['password']
            if (db.legitLogin(user,pwrd) == False): ##if there is an error
                flash("Invalid username or password")
                return render_template("login.html")
            else:
               session["user"]=user
               ##if they hit login from another page, it should rediect them back to that page somehow
               return redirect("/about")
   ##if they're already logged in

   if "user" in session:
        flash("Please logout before you try to log into another account")
        return render_template('home.html')
   if request.method=="GET":
        return render_template("login.html")

   else:
        user = request.form['user']
        pwrd = request.form['pwrd']
        if (db.legitLogin(user,pwrd)):
            session['user']=user
            if 'return_to' in session:
                s = session['return_to']
                session.pop('return_to',None)
                return redirect(s)
            else: return redirect('/home')
        else:
            flash('Please enter a valid username and password')
            return render_template('login.html')

#LOGOUT:
@app.route("/logout", methods=['GET', 'POST'])
def logout():
   if request.method == "GET":
      session.pop('user',None)
      render_template('logout.html')
   else:
      return redirect('/login')

#REGISTER:
@app.route("/register", methods=['GET', 'POST'])
def register():
   if "user" in session:
      flash("You're already logged in! If you want to register for another account, please logout first")
      return render_template('home.html')
   if request.method=='GET':
        return render_template("register.html")
   else:
      user = request.form["user"]
      pwrd = request.form["pwrd"]
      if (not(db.legitLogin(user,pwrd))):
        flash("Invalid username or password")
        redirect("/login")   
      elif (db.existingUser(user)==False):
        flash("That username is already taken, try another one")
        redirect("/login")
      else:

         user = request.form["user"]
         pwrd = request.form["pwrd"]
         ##name = request.form["name"]

         if (not(db.legitLogin(user,pwrd))):
            flash("Invalid username or password")
            redirect("/register")   
         elif (db.existingUser(user)):
            flash("That username is already taken, try another one")
            redirect("/register")
         else:
            db.user.insert({"user":user, "pwrd":pwrd, "name":name})
            redirect("/login")           
            db.registerUser(user,pwrd)
            flash("You have succesfully created a new account! Please log in to continue")
            return redirect('/login')
            #Notsurewhat these are doing:
            #else:
            #return redirect('/home')

#SECRET PAGE 1:
@app.route("/shhh")
def page1():
   if "user" not in session:
      redirect("/login")
   else:
      return render_template("secret1.html")

#SECRET PAGE 2:
@app.route("/shhh2")
def page2():
   if "user" not in session:
      redirect("/login")
   else:
      return render_template("secret2.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
    
        
