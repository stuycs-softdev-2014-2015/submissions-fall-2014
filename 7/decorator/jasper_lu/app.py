from flask import Flask

from flask import session,url_for,request,redirect,render_template

app = Flask(__name__)
app.secret_key="my secret key"

def auth(func):
    def inner(*args):
        if 'username' in session:
            return func()
        else:
            return redirect(url_for('login'))
    return inner

@app.route("/hidden")
@auth
def hidden():
    return "<h1>You are logged in!</h1>"


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="GET":
        page="""<h1>Login</h1>
        <form method="post">
        <input type="text" name="username">
        <input type="password" name="password">
        <input type="submit" name="button" value="Login">
        </form>
        """
        return page
    else:
        button = request.form['button']
        if button == 'Login':
            username = request.form['username'].encode ('ascii',"ignore")
            password = request.form['password'].encode ('ascii',"ignore")
            session['username'] = username
            return redirect ("/hidden")

@app.route("/")
def home():
    #return redirect(url_for('count'))
    return redirect("/hidden")




if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

