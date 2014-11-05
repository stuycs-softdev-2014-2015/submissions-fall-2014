from pymongo import Connection

conn = Connection()
db = conn['login']

def register(user,pword,pword2,name):
    if user == "":
        return "Please enter a username."
    if next(db.users.find({"user":user}),None) != None:
        return "The username entered is already registered."
    if pword == "" or pword2 == "":
        return "No password entered in one or more of the fields."
    if pword != pword2:
        return "The passwords entered do not match."
    if name == "":
        return "No name entered."
    list = [{"user":user,"password":pword,"name":name}]
    db.users.insert(list)
    return "Successfully registered."

def login(user,pword):
    if user == "":
        return "Please enter your username."
    if pword == "":
        return "Please enter your password."
    if next(db.users.find({"user":user}),None) == None:
        return "No such username is registered."
    if next(db.users.find({"user":user,"password":pword}),None) == None:
        return "Incorrect password."
    return "Successfully logged in."

def getinfo(user):
    return next(db.users.find({"user":user},{'_id':False,'password':False}),None);

if __name__ == "__main__":
    print "Clearing the users database"
    db.users.drop()
