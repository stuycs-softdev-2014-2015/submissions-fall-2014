from pymongo import MongoClient

client = MongoClient()
db = client.account_manager

users = db.users

# Plaintext passwords, woohoo!
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

def validate_login(username, password):
    return users.find({"username" : username, "password" : password}).count() == 1

def validate(username, password):
    if (len(username) < 1):
        return [False, "Registration error: Your username must be at least 1 character long"]
    if (len(password) < 6):
        return [False, "Registration error: Your password must be at least 6 characters long"]
    return [True, "Registration successful. Enjoy!"]


#if __name__ == "__main__":

