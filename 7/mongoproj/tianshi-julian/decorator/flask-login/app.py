#using mr.z's code

from flask import Flask,request,url_for,redirect,render_template,session,flash
from auth import auth
from functools import wraps

app=Flask(__name__)

@app.route("/")
def index():
    return "hello"

def authenticate(func):
    @wraps(func)
    def check_user(*args, **kwargs):
        (status, txt)=auth.check_user(u,p)
        if status==False:
            flash("you are not logged in")
            return render_template("login.html")
        else:
            return func(*args)
    return check_user
            

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")

    u=request.form['username']
    p=request.form['password']
    (status,txt) = auth.check_user(u,p)
    if status==False:
        flash(txt)
        return render_template("login.html")
    else:
        session['username']=txt
        n = session.pop('nextpage','/')
        return redirect(n)

@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect("/")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="GET":
        return render_template("/register.html")

    b = request.form['b']
    u = request.form['username']
    p = request.form['password']

    if b=="Cancel":
        return redirect('/')
    if u=="" or p=="":
        status=False
        txt="Specify username and password"
    else:
       (status,txt) = auth.add_user(u,p)

    if not(status):
        flash(txt)
        return render_template("/register.html")
    else:
        return redirect("/login")

@authenticate    
@app.route("/protpage1")
def protpage1():
    if 'username' not in session:
        session['nextpage']="/protpage1"
        return redirect("/login")
    else:
        return render_template("protpage1.html")

if __name__=="__main__":
   app.debug=True
   app.secret_key="hello"
   app.run(host="0.0.0.0",port=8000)
