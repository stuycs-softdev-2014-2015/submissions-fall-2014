from flask import Flask, request, session, url_for, redirect

app = Flask( __name__ )

def auth(wrapper, *args, **kwargs):
    if not 'user' in session:
        return login();
    else:
        return wrapper( *args, **args)


@app.route("/login", methods = ['GET', 'POST' ])
def login():
    if method == "GET":
        return """
            <form>
                username: <input type="text" name="user">
                password: <input type="text" name="pass">
            </form>

        """
    else:
        session['user'] = request.form['user'] 

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect( url_for("/index") )

@app.route("/Otherpage")
@auth
def otherpage():
    return """
            Hi
            <a href="/logout"> Log out and test @auth</a>
        """
@app.route("/")
@auth
def index():
    return """
        <h1>
            Welcome to a winter wonderland
            <a href="/Otherpage">Here</a>
        </h1>
    """


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5000")
