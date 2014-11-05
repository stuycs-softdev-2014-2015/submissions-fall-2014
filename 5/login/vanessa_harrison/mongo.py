from pymongo import Connection

conn = Connection()
db = conn["buttqs"]

def add(username, password, periphery):
    exists = db.users.find_one({"username":username}) != None
    if not exists:
        periphery["username"] = username
        periphery["password"] = password
        db.users.insert(periphery)
    return exists

def get(username, password):
    return db.users.find_one({"username":username, "password":password})
