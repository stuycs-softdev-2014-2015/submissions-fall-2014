from flask import Flask
from flask import session, url_for, request, redirect, render_template
import authen

app = Flask(__name__)
app.secret_key = "as124fa6s3426joijtoq124wm10525e"


@app.route("/")
def home():
    return redirect("/login")

def auth(func):
    def wrapper():
        if 'name' in session:
            return func()
        else:
            return redirect("/unknown")
    return wrapper


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET" :
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii", "ignore")
        button = request.form['button']
        if button == "Login":
            if authen.authenticate(username,password):
                session["name"] = username
                return redirect("/members")
            else:
                 return redirect("/unknown")
        elif button == "Cancel":
            return render_template("login.html")
        
        
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET" :
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword'].encode("ascii","ignore")
        security = request.form['security']
        answer = request.form['answer']
        button = request.form['button']
        if button == "Submit":
            #if accounts.has_key(username):
               # return render_template("register.html", message = "There is already an account under your name.")
            if (username == '' or password == '' or confirmpassword == '' or answer == ''):
                return render_template("register.html", message = "Please fill empty fields")
            elif password != confirmpassword:
                return render_template("register.html", message = "Please enter the same passwords.")
            else:
                if(authen.register(username,password,security,answer)):
                    session["name"] = username    
                    return redirect("/members")
                else:
                    return render_template("register.html", message = "There is already an account under your name.")
        elif button == "Cancel":
            return render_template("register.html")


@app.route("/members")
@auth
def members():
    return render_template("members.html", d = session)

@app.route("/logout")
def logout():
    session.pop('name')
    return redirect("/")
    
@app.route("/unknown")
def unknown():
    page = """
    <h2> You need to login in</h2>
    <a href="/login">Login here!</a>
    <br>
    <a href="/register">Don't have an account?</a>
    """
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
