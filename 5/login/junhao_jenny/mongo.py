import datetime, utils
from pymongo import MongoClient

db = MongoClient().junhaojenny
accounts = db.accounts

def registerErrors(user, password):
    query = accounts.find({'user':user})
    if query.count() > 0:
        return "Username taken"
    if not utils.isValidPass(password):
        return "Password must have more than 4 characters and include a digit"
    return None

def loginErrors(user, password):
    dict = {'user':user,'password':password}
    query = accounts.find(dict)
    if query.count() == 0:
        query = accounts.find({'user':user})
        if query.count() == 0:
            return "Username does not exist"
        else:
            return "Incorrect password"
    return None

def addAccount(user, password):
    dict = {'user':user,'password':password}
    dict['date_created'] = datetime.date.today().strftime("%B %d, %Y")
    accounts.insert(dict)
