from flask import Flask, render_template, request,redirect, session, url_for,session,escape,request, flash
from functools import wraps

import MongoWork
app = Flask(__name__)
app.secret_key = 'Really secret but not really' #just for session usage

def authenticate(f):
    @wraps(f)
    def wrap(*args):
        if 'username' in session:
            return f(*args)
        else:
            flash("You must log in to see that page.")
            return redirect(url_for('index',redirect_user = True))
    return wrap

@app.route("/", methods=["POST","GET"])
def index():
    error = None
    if request.method == 'POST':
        userinput = request.form['user']
        pwdinput = request.form['passwd']
        #print MongoWork.check_user_in_db(userinput)
        if MongoWork.check_user_in_db(userinput) != None:
            if MongoWork.find_pword(userinput) == pwdinput: ##SUCCESSFULLY LOGGED IN
                session['username'] = userinput
                redirect_necessary = request.args.get('redirect_user')
                if redirect_necessary:
                    return redirect(url_for("user"))
                else:
                    return redirect(url_for('dashboard',username=userinput))
            else:#incorrect password error
                error = True
                return render_template("index.html" ,error=error)
        else:
            #print "not in users"
            notreg = True
            return render_template("index.html", notreg = notreg)
    else:#request.method == "GET"
        error = None
        return render_template("index.html")

#can be viewed without logging in
@app.route("/about", methods=["POST","GET"])
def about():
    if 'username' in session:
        loggedin = True
        username = escape(session['username'])
        return render_template("about.html", loggedin=loggedin,username=username)
    else:
        loggedin = False
    return render_template("about.html", loggedin=loggedin)


@app.route("/loggedin/", methods=["POST","GET"])
@authenticate
def user():
    #POST METHOD MEANS UPDATING PASSWORD
    if request.method == 'POST':
        newpwdinput = request.form.get("newpas")
        newrepwdinput = request.form.get("newrepas")
        if newpwdinput == newrepwdinput: #matched successfully, update passwords
            username = escape(session['username'])
            MongoWork.update_password(username,newpwdinput)
            flash("Password was successfully updated.")
            return redirect(url_for("user"))
        else:
            flash("Passwords did not match. Password was not updated.")
            return redirect(url_for("user"))
    else: #GET METHOD
        username = escape(session['username'])
        user_info = MongoWork.find_usrinfo(username)
        fname = user_info['firstname']
        lname = user_info['lastname']
        u = user_info['uname']
        pwd = user_info['password']
        return render_template("user.html",username=username,fname=fname, lname=lname,u=u,pwd=pwd); 
    
@app.route("/dashboard")
@authenticate
def dashboard():
    username = escape(session['username'])
    return render_template("dashboard.html",username=username)

#must pop off session
@app.route("/logout")
def logout():
    #remove username from session
    session.pop('username', None)
    return redirect(url_for('index'))
        

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        usr = request.form['username']
        passw = request.form['passwd']
        repassw = request.form['repasswd']
        firstname = request.form['fname']
        lastname = request.form['lname']
        if passw == repassw and usr!='' and passw!='' and firstname!='' and lastname!='':#checks if everything is filled out
            #retVals = ' %s , %s, %s, %s , %s ' % (usr, passw, repassw, firstname, lastname)
            mongo_input = { 'uname':usr,
                            'password':passw, 
                            'firstname':firstname,
                            'lastname':lastname } 
            #print mongo_input
            #print MongoWork.check_user_in_db(usr)
            if MongoWork.check_user_in_db(usr):
                user_taken=True
                return render_template("register.html",user_taken=user_taken, usr=usr)
            else:####SUCCESS!
                MongoWork.new_user(mongo_input) #put user into our mongodb
                registered = True
                return redirect(url_for("index",registered=registered)) 
        else: #aka passwd !=repassw OR not all filled out
            if passw != repassw:#pwd and re-type pwd fields do not match
                reg_error = True
                return render_template("register.html", reg_error=reg_error)
            else:#missing field error
                empty=True
                return render_template("register.html", empty=empty)
    else:#GET method
        return render_template("register.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
