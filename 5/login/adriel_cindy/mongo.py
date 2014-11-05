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
<<<<<<< HEAD
	if(db.users.find({"user": u}).limit(1).count() > 0):
		return True
=======
	if(db.myDocs.find({"mykey": {"$exists": True}}).limit(1).count() > 0):
            return True
>>>>>>> 872cf02aa44da1d1b52c69bc2fa7ee41c2026f10
	return False

#Test stuff here
#add_user("hi","bye")
#print exists_user("hi")

#get_password("hullo")
#get_password('hi')
#res = db.users.find({},{'_id':False})
#for r in res:
#    print r
