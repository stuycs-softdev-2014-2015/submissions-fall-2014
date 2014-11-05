from flask import Flask, render_template, request, url_for, redirect, session, flash
import mongo
import datetime

changed = False
today = datetime.date.today()
today = today.strftime('%A, %B %dth, %Y')
time = datetime.datetime.now().time()
time = time.strftime("%I:%M")

app = Flask(__name__)
app.secret_key = '\x80\xd5\xae\x8eJ\xff&\xbe\xd6\x00\xe6\xf3\x18Y\xda@x\xeb\xa9j\xba\xe6\xedX'
@app.route("/register", methods=["GET","POST"])
def register():
        if request.method=="GET":
                return render_template("register.html", 
                    account=False, pword=False)
        else:
                if request.form['b']=="Register":
                        username = request.form['username']
                        pword = request.form['password']
                        pword_confirm = request.form['password_confirm']
                        first_name = request.form['first_name']
                        last_name = request.form['last_name']
                        if (pword == pword_confirm):
                                if (mongo.add_account(username, pword,first_name,last_name)):
                                        session['username'] = username
                                        session['password'] = pword
                                        session['first_name'] = first_name
                                        session['last_name'] = last_name
                                        return redirect(url_for('user_home', changed=False, today = today, time=time))
                                else:
                                    return render_template("register.html", 
                                        account=True, pword=False)
                        return render_template("register.html",
                            account=False, pword=True)
                if request.form['b']=="Cancel":
                        return redirect(url_for('login', alert=False))
                if request.form['b']=="Log In":
                    return redirect(url_for("login"))
                if request.form['b']=="About":
                    return redirect(url_for("about"))
                

   
@app.route("/home", methods=["GET", "POST"])
def user_home():
        if 'username' in session:
            if request.method=="GET":
                return render_template("user_home.html", changed=changed, today=today, time=time)
            else:
                if request.form['b']=="Log Out":
                    return redirect(url_for("logout"))
                if request.form['b']=="About":
                    return redirect(url_for("about"))
                if request.form['b']=="Manage Account":
                    return redirect(url_for("manage_account", alert=False))
        else:
            return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('first_name', None)
    session.pop('last_name', None)
    return redirect(url_for('login'))


@app.route("/",methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html", alert=False)
    else:
        if request.form['b']=="About":
            return redirect(url_for("about"))
        if request.form['b']=="Sign Up":
            return redirect(url_for("register"))
        if "Cancel" == request.form['b']:
                return redirect(url_for("login", alert=False))
        if "Log In" == request.form['b']:
            uname  = request.form['username']
            pword  = request.form['password']
            if (mongo.check_user(uname, pword)):
                session['username']=request.form['username']
                session['password']=request.form['password']
                account = mongo.get_account(uname)
                session['first_name']=account['first_name']
                session['last_name']=account['last_name']
                return redirect(url_for('user_home', changed=False, today=today, time=time))
            else :
                return render_template("login.html", alert=True)
        
@app.route("/manage_account", methods=["GET", "POST"])
def manage_account():
    if 'username' in session:
        username = session['username']
    if request.method=="GET" or request.form['b']=="Cancel":
        return render_template("manage_account.html", alert=False)
    else:
        if request.form['b']=="Submit":
            old_password = request.form['old_password']
            new_username = request.form['username']
            new_password = request.form['password']
            confirm_password = request.form['password_confirm']
            if new_password == confirm_password and old_password == session['password']:
                if (mongo.update_account(username, new_username, new_password)):
                    session['username'] = new_username
                    session['password'] = new_password
                    return redirect(url_for("user_home", changed=True, today=today, time=time))
            else:
                return render_template("manage_account.html", alert=True)
        if request.form['b']=="About":
                return redirect(url_for("about"))
        if request.form['b']=="Log Out":
            return redirect(url_for("logout"))
        if request.form['b']=="Home":

            return redirect(url_for("user_home", changed=False, today=today, time=time))

@app.route("/about", methods=["GET","POST"])
def about():
        logged_in = False
        if 'username' in session:
            username = session['username']
            logged_in = True
        if request.method=="GET":
                return render_template("about.html", logged_in=logged_in)
        else:
                if request.form['b']=="Log In":
                        return redirect(url_for("login", alert=False))
                if request.form['b']=="Sign Up":
                        return redirect(url_for("register"))
                if request.form['b']=="Home":
                        return redirect(url_for("user_home", changed=False, today=today, time=time))
                if request.form['b']=="Log Out":
                        return redirect(url_for("logout"))
                                        
if __name__ == "__main__":
        app.debug=True
        app.run()


