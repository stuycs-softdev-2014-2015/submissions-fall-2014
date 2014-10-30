import pymongo

def establish_connection():
    conn = Connection('')
    db = conn.admin
    return db

def add_account(username,password): #registration
    db = establish_connection()
    db.users.insert({name:username,pw:password})

def login(username,password):
    db = establish_connection()
    res = db.authenticate(username,password)
    if (res == 1):
        return True
    return False
