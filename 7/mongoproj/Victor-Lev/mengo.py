from pymongo import MongoClient

client = MongoClient('localhost',27017)
db=client.proj
users=db.users

def new_user(username, password, studentid, pizza):
    if find_user(username) == None:
        user={
            'username':username,
            'password':password,
            'studentid':studentid,
            'pizza':pizza,
            }
        users.insert(user)
        return True
    else:
        return False

def find_user(username):
    user = users.find_one({'username':username})
    return user

def get_password(username):
     user = users.find_one({'username':username})
     return user['password']
def get_id(username):
     user = users.find_one({'username':username})
     return user['studentid']
def get_pizza(username):
     user = users.find_one({'username':username})
     return user['pizza']


def authenticate(username,password):
    user=find_user(username)
    if user==None:
        return False
    elif str(user['username']) != username or str(user['password']) != password:
        return False
    else:
        return True

