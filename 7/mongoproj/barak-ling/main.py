import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request

app = Flask(__name__)

# DON'T DO THIS, IT'S JUST FOR REFERENCE
# mongod --dbpath ../barak-ling/database

# Create a MongoClient to the running mongod instance.
# Assumes that a MongoDB instance is running on default host and port
# http://api.mongodb.org/python/current/tutorial.html
client = MongoClient()

#declares a database for users
db = client.user_database

#declares a collection of users
users = db.users


#testing a user document
#user = {"username":"user1",
#        "password":"qwer"}
#user2 = {"username":"user2",
#        "password":"tyui"}
#adding a user document to the collection
#user_id = users.insert(user)
#user_id = users.insert(user2)

#print users.find_one({"username":"user3"})

# kill the current database
# db.dropDatabase()

#for now, home page is login page
@app.route('/')
@app.route('/home')
@app.route('/login')
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user(username,password):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template("login.html")

    #pass

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.debug=True
    app.run(port = 5005)
    
