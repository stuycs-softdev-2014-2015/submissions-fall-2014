import random
#from pymongo import Connection--Deprecated
from pymongo import MongoClient

conn = MongoClient()
db = conn['sydandrew']
users = db.users

def addNewUser(uname, pword, pic):
    #check if both items are not empty
    #check if it does not equal anything in the collection 
    if db.users.find_one({"username": uname}) == None:
        newuser = {'username': uname, 'password': pword, 'picture': pic}
        if uname != '' and pword != '':
            db.users.insert(newuser)
            return [True, "Congrats, you have now joined the website"]
        else:
            return [False, "Error: You did not enter a valid username or password"]
    else:
        return [False, "Error: That username already exists, please try again"]

    #if returns false should reload the page
    # if returns true the user should then be allowed to login 



def loginUser(uname, pword):
    if db.users.find_one({'username':uname, 'password':pword}) == None:
        return [False, "Incorrect username or password"]
    else:
        print(db.users.find_one({'username':uname, 'password':pword}))
        return [True]
        # in the app.py should now redirect there 
    #check that it matches the existing thing 
