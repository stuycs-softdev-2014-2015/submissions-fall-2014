from flask import Flask, render_template, request, redirect, session

#http://runnable.com/Uhf58hcCo9RSAACs/using-sessions-in-flask-for-python

app = Flask(__name__)
id=0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

#login page
@app.route("/")
def index():
    return render_template ("login.html")

@app.route("/register")
def register():
    return render_template ("register.html")
    

@app.route('/logout')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
