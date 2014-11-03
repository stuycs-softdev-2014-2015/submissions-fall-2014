from pymongo import Connection

conn = Connection()
db = conn["butts"]

def add(username, password):
    db.users.insert({"username":username, "password":password})
    print [x for x in db.users.find()]
