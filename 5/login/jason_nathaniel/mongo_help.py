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
    else:
        print("User exists")
        
def user_exists(username):
    return users.find({"username" : username}).count() > 0
    
def remove(username):
    users.remove({"username" : username})
    
def authenticate(username,password):
    if(user_exists(username)):
        s = users.find({"name": username},{"_id": False})
        return s['password'] == password
    else:
        return -1
        
#if __name__ == "__main__":
