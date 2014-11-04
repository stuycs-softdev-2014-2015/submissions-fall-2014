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
        return [True, "Registration successful. Enjoy!"] 
    else:
        return [False, "Registration error: A user with that name already exists."]

def user_exists(username):
    return users.find({"username" : username}).count() > 0

def remove(username):
    users.remove({"username" : username})

#if __name__ == "__main__":

