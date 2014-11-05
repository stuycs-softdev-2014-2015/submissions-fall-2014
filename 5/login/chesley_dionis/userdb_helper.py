from pymongo import MongoClient

client = MongoClient()
db = client.account_manager

users = db.users

# Plaintext passwords, woohoo!
def insert(username, password):
    if (not user_exists(username)):
        new_user = {
                "username" : username,
                "password" : password,
                "name" : "N/A",
                "occupation" : "N/A",
                "age" : None
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
def getInfo(username):
    if user_exists(username):
        return users.find({"username": username},{"_id":0,"username": 0,"password": 0})
    else:
        return None
def updateInfo(username,name,job,age):
    if age != "":
        age=int(float(age))
    if(user_exists(username)):
        users.update({"username": username},{"$set":{"name": name, "occupation":job,"age":age}})
        return "Successfully updated info."
    else:
        return "User error: Somehow user doesn't exist"
#if __name__ == "__main__":

