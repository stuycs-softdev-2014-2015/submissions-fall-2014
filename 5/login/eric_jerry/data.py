from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client['saurinnn']
posts = db['posts']

#add new uname/pw to database
def addNew(username, password):
    if posts.find_one({"uname": username})==None:
        entry = {"uname": username, "pw": password}
        posts.insert(entry)
        return True
    else:
        return False

#check if user/pw matches
def check(username, password):
    user = posts.find_one({"uname": username})
    if user==None:
        return False
    else:
        return password == user.get("pw").encode('ascii','ignore')

def count():
    return posts.count()

def show():
    return posts.find()
