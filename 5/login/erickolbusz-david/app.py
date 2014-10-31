from flask import Flask, render_template, request, redirect, session

http://runnable.com/Uhf58hcCo9RSAACs/using-sessions-in-flask-for-python

app = Flask(__name__)
id=0
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


#homepage
@app.route("/")
def index():
    session['tmp'] = 43
    return '43'
    if (submit == "Submit"):
        return redirect ("")
    


if __name__ == '__main__':
    app.run()
