from flask import Flask,render_template,request,session,redirect,url_for
from pymongo import MongoClient
from functools import wraps

app = Flask(__name__)

client = MongoClient()
db = client['itsudemo']
acctdb = db['accounts']
postdb = db['posts']
replydb = db['replies']
diary = db['diary']

def loggedin():
    if ("username" in session):
        return True
    else:
        return False

def requirelogin(f):
    @wraps(f)
    def ff():
        if loggedin(): return f()
        else: return redirect("/")
    return ff

def requirelogout(f):
    @wraps(f)
    def ff():
        if not loggedin(): return f()
        else: return redirect("/")
    return ff

@app.route("/")
@app.route("/home",methods=['GET','POST'])
def home_html():
    if request.method=="POST":
        pass
    return render_template("home.html",
                           sess=session)


@app.route("/todo")
def todo_html():
    return render_template("todo.html")

@app.route("/login", methods=["GET","POST"])
@requirelogout
def login_html():
    error = []
    success = True
    post = False
    if(request.method=="POST"):
        post = True
        loguser = request.form["username"]
        logpass = request.form["password"]
        if loguser=="jamal":
            error.append("go away jamal")
        acct = acctdb.find_one({"login":loguser})
        if not acct:
            error.append("no user with that name")
        else:
            if acct["password"]!=logpass:
                error.append("wrong username or password")
        if len(error)>0:
            success = False
        else:
            session["username"] = loguser
            return redirect("/")
    return render_template("login.html",
                           errorlist=error, 
                           success=success,
                           post=post,
                           sess=session)

@app.route("/logout")
@requirelogin
def logout_html():
    session.pop('username',None)
    return redirect('/')

@app.route("/register", methods=["GET","POST"])
#@requirelogout
def register_html():
    if(request.method=="POST"):
        newuser = request.form["username"]
        newpass = request.form["password"]
        newpass2 = request.form["pwdconfirm"]
        error = []
        success = True
        post = True
        
        if newpass!=newpass2:
            error.append("mismatched password")
        if newuser=="jamal":
            error.append("you are jamal")
        if newuser=="Anonymous":
            error.append("no")
        if acctdb.find_one({"login":newuser}):
            error.append("user with that name already exists")
        if len(error)>0:
            success = False
        else:
            newAccount = {"login":newuser,"password":newpass}
            acctdb.insert(newAccount)
        return render_template("register.html",
                               errorlist=error,
                               success=success,
                               post=post)
    else:
        return render_template("register.html")

@app.route("/posts",methods=['GET','POST'])
def posts_html():
    errors = []
    post = False
    success = True
    if request.method=="POST":
        post = True
        newtitle = request.form["title"]
        newbody = request.form["body"]
        newid = postdb.count()+1
        if postdb.find_one({"title":newtitle}):
            errors.append("post with that title already exists")
        if len(errors)>0:
            success = False
        else:
            newpost = {"title":newtitle,"author":session["username"],"body":newbody,"id":newid}
            postdb.insert(newpost)
    posts = postdb.find()
    return render_template("posts.html",
                           errorlist=errors,
                           post=post,
                           success=success,
                           posts=sorted(posts,key=lambda k:k["id"] if "id" in k else 0,reverse=True),
                           sess=session)

@app.route("/post/<title>",methods=['GET','POST'])
def post_html(title):
    errors = []
    post = False
    success = True
    if request.method=="POST":
        post = True
        newbody = request.form["body"]
        newid = replydb.find({"title":title}).count()+1
        if len(newbody)==0:
            errors.append("blank reply")
        if len(errors)>0:
            success = False
        else:
            newreply = {"title":title,"author":session["username"],"body":newbody,"id":newid}
            replydb.insert(newreply)
    replies = replydb.find({"title":title})
    return render_template("post.html",
                           errorlist=errors,
                           post=post,
                           success=success,
                           replies=sorted(replies,key=lambda k:k["id"] if "id" in k else 0),
                           sess=session,
                           op=postdb.find_one({"title":title}))

@app.route("/settings",methods=['GET','POST'])
@requirelogin
def settings_html():
    errors = []
    post = False
    success = True
    if request.method=="POST":
        post = True
        oldpass = request.form["oldpass"]
        newpass = request.form["newpass"]
        passcfm = request.form["passcfm"]
        curacct = acctdb.find_one({"login":session["username"]})
        curpass = curacct["password"]
        if oldpass!=curpass:
            errors.append("incorrect password")
        if newpass!=passcfm:
            errors.append("new passwords don't match")
        if len(errors)>0:
            success = False
        else:
            curacct["password"] = newpass
            acctdb.save(curacct)
    return render_template("settings.html",
                           errorlist=errors,
                           post=post,
                           success=success,
                           sess=session)

@app.route("/diary",methods=["GET","POST"])
@requirelogin
def diary_html():
    if (request.method=="POST"):
        content= request.form["content"]
        newEntry = {"author":session["username"],"content":content}
        diary.insert(newEntry)
    return render_template("diary.html",postList=diary.find({"author":session["username"]}))

###

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "insane"
    app.run()
