from flask import Flask, flash, redirect, request, render_template, url_for

app = Flask(__name__)
app.secret_key = 'dont_tell'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST' or request.mthod == 'GET':
        flash('You are now registered')
        return redirect(url_for('login'))
    else:
        #flash('Invalid username or password')
        #return redirect(url_for("register"))
        render_template('register.html')
        
if __name__ == "__main__":
    app.debug = True
    app.run()
