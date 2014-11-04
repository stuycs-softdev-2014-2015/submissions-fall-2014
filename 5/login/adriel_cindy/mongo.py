from pymongo import Connection

conn = Connection()

db = conn['Login']
#For clearing database
conn.drop_database('Login');
def add_user(u, pw):
    db.users.insert({'user':u, 'password':pw})

def update_user(u, i):
    db.users.update({'user':u}, {'$set':{'info':i}})

def get_password(u):
    l = db.users.find({'user':u})
    for u in l:
        return u['password']
    return None

#Just testing stuff
add_user("hi","bye")

#get_password("hullo")
#get_password('hi')
#res = db.users.find({},{'_id':False})
#for r in res:
#    print r
