import pymongo, hashlib
connection = pymongo.Connection()

db = connection["database"]
users = db.users
posts = db.posts

#return true if valid input; false if not
def checkPassword(passwordToCheck):
    return len(passwordToCheck) > 0

def checkUsername(usernameToCheck):
    return ((len(usernameToCheck) > 0) and (users.find({"username":usernameToCheck}).count()==0))

def checkPost(postToCheck):
    return len(postToCheck) > 0

def addUser(username, password):
    record = users.find({"username":username})
    if ((checkUsername(username) == False) or (checkPassword(password) == False)) or (record.count() != 0):
        return False
    else:
        newUser = {"username": username,"password": hashlib.sha512(password).hexdigest()}
        users.insert(newUser)
        return True

def validateUser(username, password):
    record = users.find({"username":username})
    if (record.count() != 1):
        return False
    else:
        return record[0]['password'] == hashlib.sha512(password).hexdigest()


def addPost(username, post, privacy):
    if ((checkPost(post) == False) or (users.find({"username":username}).count()<1)):
        return False
    else:
        newPost = {"username": username,"post": post, "privacy": privacy}
        posts.insert(newPost)
        return True
        
def addPublicPost(username, post):
    return addPost(username, post, "Public")    

def addPrivatePost(username, post):
    return addPost(username, post, "Private")

def getPosts(privacy):
    result = posts.find({'privacy': privacy})
    postList = []
    for post in result:
        miniPostList = []
        miniPostList.append(post['username'])
        miniPostList.append(post['post'])
        miniPostList.append(post['privacy'])
        postList.append(miniPostList)
    return postList
        
def getPublicPosts():
    return getPosts("Public")

def getPrivatePosts():
    return getPosts("Private")


