from pymongo import MongoClient

#connection = MongoClient()
#db = connection.database
connection = MongoClient('db.stuycs.org')
db = connection.admin
db.authenticate('softdev','softdev')
db = connection.database

def register(user, pw):
    if checkuser(user) == False:
        db.login.insert({'user':user, 'pass':pw})
        return True
    
def authenticate(username, password):
    user = [x['password'] for x in db.login.find({'username':username})]

    if len(user) > 0 and user[0] == password:
        return True
    else:
        return False

def authenticateOld(username,password):
    users = db.login.find({'username':username,'password':password},
                              fields={'_id':False})
    return len([user for user in users]) != 0
    
def authenticateRegister(username):
    users = db.login.find({'username':username},
                                             fields={'_id':False})
    return len([user for user in users]) != 0
    
def checkuser(user):
    users = [user for user in db.login.find({'user':user},
                                            fields={'_id':False,'user':True})]
    return len(users)!=0

def changePass(user, pw, npw):
    if login(user,pw):
        db.login.update({'user':user}, {'$set': {'pass':npw}})
        return True
    else:
        return False

def login(user, pw):
    users = [user for user in db.login.find({'user':user}, 
                                           fields={'_id':False,'user':True, 'pass':True})]
    return users[0]['pass'] == pw
