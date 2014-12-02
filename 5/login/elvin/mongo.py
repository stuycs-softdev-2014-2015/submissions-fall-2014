from pymongo import MongoClient
import hashlib
from tools import valid_password

db = MongoClient('mongodb://localhost:27017/').dataclient
users = db.users

# String constants

INVALID_USER = "Invalid username! Have you made sure to register?"
INVALID_PASS = "Invalid password! Did you make a typo?"
USER_TAKEN = "Username taken! Try to be more original."
BETTER_PASS = "Please pick a better password! Greater than 6 characters with at least one number and an uppercase."
SUCCESS_LOGIN = "You've successfully logged in as %s!"
SUCCESS_REGISTER = "You've successfully registered as %s!"

def create_user(username, password):

	# Hash the password, only the hash will be stored
	m = hashlib.sha1()
	hashing = m.update(password)
	hashed = m.hexdigest()

	user_dict = {
			'user': username,
			'pwd': hashed
		}

	search_dict = {
			'user': username
		}

	user_search = users.find(search_dict)
	
	# Such a user already exists!
	if (user_search.count() > 0):
		return (False, USER_TAKEN)
	else:
		# What about the password?
		good_pass = valid_password(password)

		if good_pass:
			# Looking good!
			users.insert(user_dict)
			return (True, SUCCESS_REGISTER % username)

		else:
			return (False, BETTER_PASS)

def authenticate_user(username, password):

	# Hash the password, check the hash
	m = hashlib.sha1()
	hashing = m.update(password)
	hashed = m.hexdigest()

	search_dict = {
		'user': username
	}

	# Search for the username
	user_search = users.find(search_dict)

	# No match?
	if (user_search.count() < 1):
		return (False, INVALID_USER)
	else:
		user_found = user_search[0]

		# Correct password?
		if (user_found['pwd'] != hashed):
			return (False, INVALID_PASS)

		else:
			return (True, SUCCESS_LOGIN % username)