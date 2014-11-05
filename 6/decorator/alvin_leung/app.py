from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "asdf"


def auth(func):
    def wrapper():
        if 'user' in session:
            return func()
        else:
            return redirect(url_for("login"))
    return wrapper
    
@app.route('/')
def index():
    return "This is the homepage"

@app.route('/login',methods=['GET','POST'])
def login(success="/"):
    if request.method == 'GET':
        return """
        <form method="POST">
        User: <input type="text" name="user">
        Pass: <input type="password" name="pass">
        <button type="submit">Submit</button>
        </form>
        """
    else:
        session['user'] = request.form['user']
        return redirect(url_for("index"))

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for("index"))


@app.route('/user')
@auth
def user():
    return "Hello %s"%(session['user'])

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0",5000)
