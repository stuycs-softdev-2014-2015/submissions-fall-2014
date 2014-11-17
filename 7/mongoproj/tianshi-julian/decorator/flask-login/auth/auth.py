from pymongo import MongoClient
client = MongoClient()
db=client.zauth

def check_user(username,password):
    res = db.users.find({'username':username})
    if res.count() != 1:
        return (False,"Invalid username")

    if res[0]['password']!=password:
        return (False,"Invalid password");

    return (True, username)



def add_user(username,password):
    res = db.users.find({'username':username})
    if res.count() != 0:
        return (False,"Username taken")

    db.users.insert({'username':username,'password':password})
    return (True,username)

    
