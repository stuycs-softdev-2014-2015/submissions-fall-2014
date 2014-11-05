from pymongo import Connection

conn = Connection()

db = conn['Login']
#For clearing database
#conn.drop_database('Login');
def add_user(u, pw):
    db.users.insert({'user':u, 'password':pw, 'login':'n', 'info':0})

def get_info(u):
    l = db.users.find({'user':u})
    for u in l:
        return u['info']
    return None

#logged in = y
#logged out = n
def login_user(u):
    db.users.update({'user':u}, {'$set':{'login':'y', 'info':get_info(u)+1}})

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
	if(db.users.find({"user": u}).limit(1).count() > 0):
		return True
	return False

#Test stuff here
#add_user("hi","bye")
#print exists_user("hi")

#get_password("hullo")
#get_password('hi')
#res = db.users.find({},{'_id':False})
#for r in res:
#    print r
