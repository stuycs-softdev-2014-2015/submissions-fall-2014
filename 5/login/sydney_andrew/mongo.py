import random
#from pymongo import Connection--Deprecated
from pymongo import MongoClient

conn = MongoClient()
db = conn['sydandrew']
users = db.users

def addNewUser(uname, pword, pic):
    if pic="1":
        pic="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHMWkgpCaI9ybEfMJZGRMMNcyoAehisCnhGrlpXl8c6fdrjNoF2rhiHAc"
    elif pic="2":
        pic="http://ngm.nationalgeographic.com/2013/04/manatees/img/01-florida-manatee-670.jpg"
    elif pic="3":
        pic="http://i.huffpost.com/gen/1273181/thumbs/o-MANATEE-900.jpg?1"
    elif pic="4":
        pic="http://i.huffpost.com/gen/1272530/thumbs/o-MANATEES-900.jpg?5"
    else:
        pic=""
    #need to be able to pick a picture 
    #check if both items are not empty
    #check if it does not equal anything in the collection 
    if db.users.find_one({"username": uname}) == None:
        newuser = {'username': uname, 'password': pword, 'picture': pic}
        if uname != '' or pword != '' or pic !='' :
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
