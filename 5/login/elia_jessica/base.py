import random
from pymongo import Connection

conn = Connection()

db = conn['1590']

def addUser(usernamei, passwordi):
    res = db.usertable.find({username:usernamei})
    if len(res)>0:
        return False
    nu = {username: usernamei, password:passwordi}
    db.usertable.save(nu)
    return True

def validate(usernamei, passwordi):
    res = db.usertable.find({username: usernamei, password:passwordi})
    if len(res)>0:
        return True
    return False

def updateUser(usernamei, passwordi):
    res = db.usertable.find({username:usernamei})
    if len(res)>0:
        return False
    db.usertable.update({username: usernamei, password:passwordi})
    return True
    
