from pymongo import Connection

conn = Connection()

db = conn['Login']
conn.drop_database('Login');
def add_user(u, pw):
    db.users.insert({'user':u, 'password':pw})

def update_user(u, i):
    db.users.update({'user':u}, {'$set':{'info':i}})

def get_password(u):
    return db.users.find({'user':u})[0]['password']

add_user("hi","bye")

get_password('hi')
#res = db.users.find({},{'_id':False})
#for r in res:
#    print r
