import datetime, utils
from pymongo import MongoClient

db = MongoClient().junhaojenny
accounts = db.accounts

def registerErrors(dict):
    newUser = dict['user']
    newPass = dict['password']
    query = accounts.find({'user':newUser})
    if query.count() > 0:
        return "Username taken"
    if not utils.isValidPass(newPass):
        return """Password must have more than 5 characters and include at least:
        1 uppercase letter
        1 lowercase letter
        1 number"""
    return None

def loginErrors(dict):
    query = accounts.find(dict)
    if query.count() == 0:
        user = dict['user']
        query = accounts.find({'user':user})
        if query.count() == 0:
            return "Username does not exist"
        else:
            return "Incorrect password"
    return None

def addAccount(dict):
    dict['date_created'] = datetime.date.today().strftime("%B %d, %Y")
    accounts.insert(dict)
