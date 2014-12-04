import pymongo
from pymongo import Connection

#
# conn = pymongo.MongoClient()
# db = conn.userDatabase
conn = Connection()
db = conn["userDatabase"]


def checkLogin(uName, pword):
    if(db.userData.find({'userName': "'"+uName+"'", 'password': "'"+pword+"'"}).count() == 0):
        return False;
    else:
        return True;
