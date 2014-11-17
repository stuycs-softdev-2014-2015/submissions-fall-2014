from pymongo import Connection

conn = Connection()
db = conn['people']

def add_user(username, name, password):
    d = {'username': username,'name':name, 'password': password}
    if check(username):
        return "error: username already there"
    else:
        db.people.insert(d)
        return "added user"
    

def authenticate(username, password):
    #check to see if username & password match, if they do, will return true
    x = db.people.find({'username':username})
    if x.count()>0:
        return x[0]['password'] == password
    return False

def check(username):
    x = db.people.find({'username':username})
    if x.count() > 0:
        return True
    return False

def getName(username):
    x = db.people.find({'username':username})
    return x[0]['name']

        
