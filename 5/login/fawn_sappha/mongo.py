from pymongo import Connection

conn = Connection()
db = conn["fawn-sappha"]
#conn.drop_database("fawn-sappha")

def adduser(u, p):
	# register
	db.accounts.insert({"username": u, "password": p})

def validusername(u):
	# register
	accounts = db.accounts.find({"username": u})
	for user in accounts:
		return False
	return True

def checkcombo(u, p):
	# returns true if valid u/p combo, false if not
	# for login
	accounts = db.accounts.find({"username": u})
	for user in accounts:
		return user["password"] == p
	#if username is not found in accounts
	return False

def changepw(u, p):
	db.accounts.update({"username": u}, {"password": p}, upsert = True)



