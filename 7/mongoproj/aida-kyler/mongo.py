from pymongo import Connection

conn = Connection()
db = conn['delta']


def add_account(username,password,first_name,last_name):
    res = db.accounts.find({"username":username})
    if res.count() != 0:
        return False
    db.accounts.insert({"username":username, "password":password, 
    	"first_name":first_name, "last_name":last_name})
    return True

def check_user(username,password):
    res = db.accounts.find({"username":username, "password":password})
    return res.count() == 1


def update_account(username, new_username, new_password):
	res = db.accounts.update(
		{"username":username},
		{ "$set": {
				"username":new_username, 
				"password":new_password, 
			}
		}
	)
	return True

def get_account(username):
    res = db.accounts.find({"username":username})
    return res.next()


