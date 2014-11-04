from pymongo import Connection

conn = Connection()
db = conn["butts"]

def add(username, password):
    exists = db.users.find_one({"username":username})
    if not exists:
        db.users.insert({"username":username, "password":password})
    return exists

def validate(username, password):
    return db.users.find_one({"username":username, "password":password}) != {}
