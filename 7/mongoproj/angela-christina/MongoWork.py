import random
from pymongo import MongoClient
#after looking at the API, it seems like using
#MongoClient is better than using Connection,
#which is depreciated
client = MongoClient()


db = client['data']#database called data
users = db['names']#collection of users
#users should have uname, password, firstname, lastname

#checks if the user is already in our users collection
def check_user_in_db(usr):
    return users.find_one({'uname':usr})

#finds the password of a given user, so we can check for validation
def find_pword(usr):
    #okay to use find_one since usernames are unique
    res = users.find_one({'uname':usr}, {'_id':False})
    return res['password']

def find_usrinfo(usr):
    #okay to use find_one since usernames are unique
    res = users.find_one({'uname':usr}, {'_id':False})
    return res

#creating a new user
def new_user(dictinput):#MUST CHECK IF USER IN DB
    users.insert(dictinput)
    #for user in users.find():
        #print user

def drop_users():
    db.drop_collection('names') #drops collection each time --> this should not be necessary in the future but...

def update_password(usr,newpwd):
    users.update({'uname':usr},{'$set':{'password':newpwd}}, upsert=False, multi=False)

