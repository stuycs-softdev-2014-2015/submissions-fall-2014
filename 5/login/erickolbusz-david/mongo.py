from pymongo import Connection

def establish_connection():
    conn = Connection('')
    db = conn.admin
    return db

def add_account(username,password): #registration
    db = establish_connection()
    db.users.insert({'name':username,'pw':password,'logincount':1})

def login(username,password):
    db = establish_connection()
    res = db.authenticate(username,password)
    if (res == 1):
	user_list = db.users.find({'name':username, 'pw':password})
	if (len(user_list)>1) :
		print("TWETHJASUIFHIOSE") #more than one account with that username and password
		exit(1) #?!??!?!?!?!?????//
	user = user_list[0]
	new_login_count = user['logincount'] + 1
	users.update({'name':username, 'pw':password, 'logincount':new_login_count}, upsert=True)
        return True
    return False
