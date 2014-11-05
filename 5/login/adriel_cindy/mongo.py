from pymongo import Connection

conn = Connection()

db = conn['Login']
#For clearing database
conn.drop_database('Login');
def add_user(u, pw):
    db.users.insert({'user':u, 'password':pw, 'login':'n'})

def update_user(u, i):
    db.users.update({'user':u}, {'$set':{'info':i}})

#logged in = y
#logged out = n
def login_user(u):
    db.users.update({'user':u}, {'$set':{'login':'y'}})

def logout_user(u):
    db.users.update({'user':u}, {'$set':{'login':'n'}})

def logged_in(u):
    l = db.users.find({'user':u})
    for u in l:
        return u['login']
    return None

def get_password(u):
    l = db.users.find({'user':u})
    for u in l:
        return u['password']
    return None

def exists_user(u):
	if(db.myDocs.find({"mykey": {"$exists": True}}).limit(1).count() > 0):
            return True
	return False

#Just testing stuff
add_user("hi","bye")

#get_password("hullo")
#get_password('hi')
#res = db.users.find({},{'_id':False})
#for r in res:
#    print r
