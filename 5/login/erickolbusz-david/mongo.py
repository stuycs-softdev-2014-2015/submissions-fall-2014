from pymongo import Connection

def establish_connection():
    conn = Connection('')
    db = conn.admin
    return db

def add_account(username,password): #registration
    db = establish_connection()
    does_account_exist = db.authenticate(username)
    if (does_account_exist == 1):
        return 1 #tried registering with taken username
    if (len(username)<6):
        return 2 #username too short
    if (len(password)<8):
        return 3 #password too short
    db.users.insert({'name':username,'pw':password,'logincount':1})
    return 0

def login(username,password):
    db = establish_connection()
    res = db.authenticate(username,password)
    if (res == 1):
        user_list = db.users.find({'name':username, 'pw':password})
	user = user_list[0]
	new_login_count = user['logincount'] + 1
	users.update({'name':username, 'pw':password, 'logincount':new_login_count}, upsert=True)
        return True
    return False
