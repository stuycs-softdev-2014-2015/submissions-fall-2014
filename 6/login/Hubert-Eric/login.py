"""Module used for dealing with database stuff"""
from pymongo import Connection


"""Json Object Values"""
nameKey = 'name'
passwordKey = 'password'
authenticatedKey = 'authenticated'


def login(name, password, dbname="users", dbCollectionName="people"):
    """string name, string password, string dbname="users",
    string collection="people"

    sets authenticated to True for a given user"""
    success = False

    conn = Connection()
    db = conn[dbname]

    people = db[dbCollectionName]

    if (isInDatabase(name, dbname, dbCollectionName)):
        # should only loop through once
        for user in people.find({nameKey: name}):
            if (user[passwordKey] == password):
                success = updateUser(name, True, dbname, dbCollectionName)

    return success


def logout(name, dbname="users", dbCollectionName="people"):
    """sets authenticated to False for a given user"""
    success = updateUser(name, False, dbname, dbCollectionName)
    return success

def authenticated(name, dbname="users", dbCollectionName="people"):
    """Checks if user is authenticated"""
    conn = Connection()
    db = conn[dbname]
    people = db[dbCollectionName]

    if (isInDatabase(name, dbname, dbCollectionName)):
        # should only loop through once
        for user in people.find({nameKey: name}):
            if (user[authenticatedKey] == True):
                return True
            return False

def updateUser(name, authenticated, dbname="users", dbCollectionName="people"):
    """string name, Boolean authenticated, string dbname, string dbCollectioName
    Logs the user in if authenticated is True
    Logs the user out if authenticated is False

    Returns True if successful or False if not successful"""
    success = True

    conn = Connection()
    db = conn[dbname]

    people = db[dbCollectionName]

    if (isInDatabase(name, dbname, dbCollectionName)):
        people.update({nameKey: name},
                      {"$set": {authenticatedKey: authenticated}},
                      False)
    else:
        success = False

    return success


def addUser(name, password, dbname="users", dbCollectionName="people"):
    """string name, string password, string dbname, string dbCollectionName
    adds user to the database and returns False is username already exists

    automatically logs the user in after creating the account"""
    success = True

    conn = Connection()
    db = conn[dbname]

    if (not isInDatabase(name, dbname, dbCollectionName)):
        # Jsonifies the User, authenticated True means the user is logged in
        user = {nameKey: name,
                passwordKey: password,
                authenticatedKey: True}
        people = db[dbCollectionName]
        people.insert(user)
    else:
        success = False

    return success


def isInDatabase(name, dbname="users", dbCollectionName="people"):
    """takes string name, string dbname, string dbCollectionName
    checks if user is already in the database and returns False if username
    already exists"""
    conn = Connection()
    db = conn[dbname]

    # returns collection of users
    people = db[dbCollectionName]

    # there should be at most one instance of the user in the database
    success = (people.find({nameKey: name}).count() == 1)

    return success


def main():
    pass

if __name__ == '__main__':
    main()
