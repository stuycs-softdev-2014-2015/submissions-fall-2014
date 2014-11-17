from pymongo import Connection
from functools import wraps

conn = Connection()
db_name="zabari_is_the_man"
col_users="users"
db = conn[db_name]
print "db init"

class User(object):
	def __init__(self, username, info):
		#username is a string. info is a dictionary containing the user's information.
		set_username(username)
		set_password(info['password'])
	def set_username(self,username):
		self.username=username
	def set_password(self,password):
		self.password=password
	def jsonify(self):
		D = { 	'username' : self.username,
			'password' : self.password
			}
		return D


def restricted(check):
	def decorate(f):
		if check=="admin":
			def inner(*args,**kwargs):
				return f
			return inner
		else:
			return f

def update_user(check=""):
	@restricted(check)
	def update(user):
		if user is User :
			users = db[col_users]
				

update_admin = update_user("admin")
update_reg = update_user("")



 
