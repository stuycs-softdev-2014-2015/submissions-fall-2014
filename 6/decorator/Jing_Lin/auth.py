from pymongo import MongoClient
c = MongoClient('db.stuycs.org')
db=c.admin
db.authenticate('softdev','softdev')
db = c.pd6
def authorize(username, password):
    return len(list(db.Collections.find({'username':username, 'password':password}))) == 1
def userExists(username):
    return len(list(db.Collections.find({'username':username}))) == 1
def createUser(username, password):
    if not userExists(username):
        db.Collections.insert({'username':username, 'password':password})
        return True
    else:
        return False
