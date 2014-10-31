from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return render_template ("index.html")% escape(session['username'])
    else:
        return """
    You are not logged in
    <br>
    <a href = "/login"> <input type = "submit" value= "Login"></a>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
#this is fake very fake oooh
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.debug = True
    app.run()
