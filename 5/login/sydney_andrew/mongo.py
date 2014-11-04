import random
from pymongo import Connection

conn = Connection()
db = conn['sydandrew']
users= db.users

def addNewUser(uname, pword, pic):
    #need to be able to pick a picture 
    #check if both items are not empty
    #check if it does not equal anything in the collection 
    if db.users.find_one()==None:
        newuser = {'username': uname, 'password': pword, 'picture': pic}
        if uname != '' or pword != '':
            db.users.insert(newuser)
            return [True, "Congrats, you have now joined the website"]
        else:
            return [False, "Error: You did not enter a valid username or password"]
    else:
        return [False, "Error: That username already exists, please try again"]

    #if returns false should reload the page
    # if returns true the user should then be allowed to login 



def loginUser(uname, pword):
    if db.users.find({'username':uname, 'password':pword})==None:
        return [False, "Sorry, there was an error when you entered your username or password"]
    else:
        return [True]
        # in the app.py should now redirect there 
    #check that it matches the existing thing 

