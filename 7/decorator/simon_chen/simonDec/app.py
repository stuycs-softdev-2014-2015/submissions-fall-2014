from flask import Flask, render_template,session,redirect,request
import auth

app = Flask(__name__)
app.secret_key='asdgasdgadsgads'

@app.route("/")
@auth.check
def index():
    return "Hello"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    else:
        username = request.form['username'].encode('ascii','ignore')
        password = request.form['password'].encode('ascii','ignore')
        print username
        print password
        if username == "user" and password == "password":
            session['username'] = username
            return redirect('/')
        return False
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)

    

