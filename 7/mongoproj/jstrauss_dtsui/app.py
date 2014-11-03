# Justin Strauss and Derek Tsui
# Software Development Period 7
# MongoDB Project

import db
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
    if "name" not in session:
        session["name"] = None
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        #if authenticate(username,password):
        if db.authenticate(username,password):
            session['name'] = username
            global prevpage
            page = prevpage
            prevpage = "index"
            return redirect(url_for(page))
        else:
            if db.userexists(username):
                flash("You've inputted the wrong password for the given user.")
                return redirect(url_for('login'))
            else:
                flash("The username you inputted hasn't been registered yet.")
                return redirect(url_for('register'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    return redirect(url_for('index'))

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        pw = request.form["password"]
        pw2 = request.form["password2"]
        if pw != pw2:
            flash("The passwords you submitted don't match, please try again.")
            return redirect(url_for('register'))
        if db.userexists(username):
            flash("The username you submitted is already taken, please try again.")
            return redirect(url_for('register'))
        if db.emailexists(email):
            flash("The email you submitted already has an account tied to it, please try again.")
            return redirect(url_for('register'))
        else:
            db.adduser(username,email,pw)
            flash("You've sucessfully registered, now login!")
            return redirect(url_for('login'))
    else:
        if session['name']!=None:
            flash("You're already logged in, so you can't register for a second account!")
            return redirect(url_for(prevpage))
        return render_template("register.html")

@app.route("/user", methods=["POST","GET"])
def myself():
    if request.method == "GET":
        if session["name"]==None:
            flash("You must login to access Profile, which is a protected page!")
            global prevpage
            prevpage = "profile"
            return redirect(url_for('login'))
        else:
            profile=db.getprofile(session['name'])
            #print profile
            posts = db.getposts(session['name'])
            return render_template("profile.html",profile=profile, posts=posts)
    else:
        newpw = request.form["newpassword"]
        newpw2 = request.form["newpassword2"]
        if (newpw != newpw2):
            flash("The new passwords you submitted don't match, please try again.")
            return redirect(url_for('profile'))
        else:
            db.updatepw(session['name'],newpw)
            flash("Your password has been sucessfully changed. Please re-login.")
            return redirect(url_for('logout'))

@app.route("/user/<username>")
def user(username):
    if session["name"]==None:
        flash("You must login to access Profile, which is a protected page!")
        global prevpage
        prevpage = "profile"
        return redirect(url_for('login'))
    else:
        profile=db.getprofile(username)
        #print profile
        posts = db.getposts(username)
        return render_template("profileother.html",profile=profile,posts=posts)

@app.route("/blog", methods=["POST","GET"])
def blog():
    if request.method == "GET":
        if session["name"]==None:
            flash("You must login to access Blog, which is a protected page!")
            global prevpage
            prevpage = "blog"
            return redirect(url_for('login'))
        else:
            blog=db.getblog(session['name'])
            print blog
            return render_template("blog.html",blog=blog)
    else:
        title = request.form["title"]
        content = request.form["content"]
        if db.invalidpost(title, content):
            flash("A post of this title already exists or there is no content!")
            return redirect(url_for('blog'))
        else:
            db.addpost(title,session['name'],content)
            flash("You have successfully made a blog post!")
            return redirect(url_for('blog'))

@app.route("/blog/<title>", methods=["POST","GET"])
def blogcontent(title):
    if request.method == "GET":
        if session["name"]==None:
            flash("You must login to access Blog, which is a protected page!")
            global prevpage
            prevpage = "blog"
            return redirect(url_for('login'))
        else:
            blogcontent=db.getblogcontent(title)
            print blogcontent
            return render_template("blogcontent.html",title=title,blogcontent=blogcontent)
    else:
        comment = request.form["comment"]
        if db.invalidcomment(comment):
            flash("There is no text in your comment!")
            return redirect(url_for('blog'))
        else:
            db.addcomment(title,session['name'],comment)
            flash("You have successfully made a comment!")
            return redirect(url_for('blog'))

@app.route("/contacts")
def contacts():
    if session["name"]==None:
        flash("You must login to access Contacts, which is a protected page!")
        global prevpage
        prevpage = "contacts"
        return redirect(url_for('login'))
    else:
        contacts=db.getcontacts(session['name'])
        print contacts
        return render_template("contacts.html",contacts=contacts)

if __name__ == '__main__':
    db.setup()
    prevpage = "index"
    app.secret_key = "don't store this on github"
    app.debug = True
    app.run(host='0.0.0.0')
