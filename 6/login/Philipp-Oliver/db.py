from pymongo import MongoClient
from hashlib import sha512
from bson.objectid import ObjectId

def connect():
    conn = MongoClient()
    db = conn["oliver-philipp"]
    return db

def extract_object_id(object_id):
    user_id_in_stupid_format = object_id.__repr__()
    first_stupid_quote = user_id_in_stupid_format.index("'")
    second_stupid_quote = user_id_in_stupid_format.index("'", first_stupid_quote + 1)
    uid = user_id_in_stupid_format[first_stupid_quote + 1:second_stupid_quote]
    return uid

def password_correct(password, username="", uid=""):
    db = connect()
    if username == "" or password == "":
        return False

    user = db.users.find_one( {"username": username})
    if user == None:
        return False

    if user["password"] == sha512(password).hexdigest(): # ObjectId' object has no attribute 'valueOf' ????????
        return extract_object_id(user["_id"])

    else:
        return False

def username_taken(username):
    db = connect()
    return db.users.find({"username":username}).count() > 0

# schedule is tuple of 10 strings
def new_user(username, password, schedule):
    db = connect()
    if username_taken(username):
        return False

    # hash the password for security
    password = sha512(password).hexdigest()

    object_id = db.users.insert({"username": username, "password":password, "schedule":schedule})
    uid = extract_object_id(object_id)
    return uid

def update_password(uid, password):
    db = connect()
    password = sha512(password).hexdigest()
    db.users.update({"_id": ObjectId(uid)}, {"password":password})

def update_schedule(uid, schedule):
    db = connect()
    db.users.update({"_id": ObjectId(uid)}, {"schedule":schedule})

