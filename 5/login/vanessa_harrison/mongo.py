from pymongo import Connection

conn = Connection()
print conn["butts"]

def add(username, password):
    conn.users.insert({"username":username, "password":password})
    print conn.users.find()
