from flask import Flask, render_template, request
from pymongo import Connection

app = Flask(__name__)
conn = Connection()
db = conn ['aaez']

@app.route("/")
def index():
    button = request.args.get("sub", None)
    username = request.args.get("username", None)
    passw = request.args.get("password", None)
    if button == "Register":
        if db.users.find_one ( { 'name' : username } ) == None:
            db.users.insert ( { 'name': username, 'pword': passw } )
            return "<h1>Thanks for joining!</h1>"
        else:
            return "<h1>Please select an available username</h1>"
    elif button == "Login":
        loginfo = { 'name': username, 'pword': passw }
        if db.users.find_one ( { 'name' : username , 'pword' : passw } ) != None:
            return "correct login info"
        return "incorrect login info"
    else:
        return render_template("index.html")


if __name__=="__main__":
    app.debug = True
    app.run()
    
