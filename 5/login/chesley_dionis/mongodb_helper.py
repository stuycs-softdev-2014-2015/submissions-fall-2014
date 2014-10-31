from pymongo import MongoClient

client = MongoClient()
db = client.account_manager

users = db.users

def insert(username, password):
    if (not user_exists(username)):
        new_user = {
                "username" : username,
                "password" : password
                }
        users.insert(new_user)
        return True
    else:
        print "User %s exists." % username
        return False

def user_exists(username):
    return users.find({"username" : username}).count() > 0

def remove(username):
    users.remove({"username" : username})

def validate(username, password):
    return users.find({"username" : username, "password" : password}).count() == 1

#if __name__ == "__main__":

