from flask import Flask, flash, redirect, request, render_template, url_for, session
from pymongo import Connection

app = Flask(__name__)
app.secret_key = 'dont_tell'

#mongostuff
conn = Connection()
db = conn['data']
users = db.posts

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ['GET','POST'])
def login():    
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #getting data from form
        button = request.form['b']
        un = request.form['username']
        pw = request.form['password']
        if button == 'cancel':
            return redirect(url_for('login'))
        elif button == 'submit':
            #authentication stuff
            dlist=[]
            plist=[]
            d = users.find()
            for i in d:
                dlist.append(i["username"])
                plist.append(i["password"])
            if un in dlist and pw in plist:
                flash('Successfully logged in!')
                return redirect(url_for('user',username = un))
            else:
                flash("Wrong username or password.")
                return render_template('login.html')
            
@app.route("/register", methods = ['GET', 'POST'])
def register():
    error = None
    if request.method == 'GET':
        return render_template('register.html')
    else:
        #getting data from form
        button = request.form['b']
        un = request.form['username']
        pw = request.form['password']
        if button == 'cancel':
            return redirect(url_for('register'))
        elif button == 'submit':
            flash('Successfully registered!')

            #adding in database
            post = {"username": un,
                    "password": pw}
            post_id = users.insert(post)
            post_id
            print db.collection_names()
            print users.find_one()
            return redirect(url_for('login'))

#individual page
@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username = username)

#url does not exist
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
        
if __name__ == "__main__":
    app.debug = True
    app.run()
