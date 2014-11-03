from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template("index.html");
    return render_template("home.html");

@app.route('/login', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        flash("You were successfully logged in")
        return redirect(url_for("home.html"))
    if 'username' in session:
        flash("You are already logged in")
        return redirect(url_for("home.html"))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out")
    return redirect(url_for("index.html"))

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.debug=True
    app.run(host="0.0.0.0", port=5678)
