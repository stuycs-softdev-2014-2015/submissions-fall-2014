from pymongo import Connection
from functools import wraps

conn = Connection()
db_name="zabari_is_the_man"
col_users="users"

db = conn[db_name]
users = db[col_users]
print "db init"

class User(object):
	def __init__(self, username, info):
		#username is a string. info is a dictionary containing the user's information.
		self.set_username(username)
		self.set_password(info['password'])
		self.set_admin(info.get('admin'))
	def set_username(self,username):
		self.username=username
	def set_password(self,password):
		self.password=password
	def set_admin(self, admin):
		self.admin = admin
	def jsonify(self):
		D = {}

		D['username']=self.username
		
		if self.password:
			D['password']=self.password
		if self.admin:
			D['admin']=self.admin
		return D

def restricted(check):
	def decorate(f):
		#This should return true if successful and false if not.
		if check=="admin":
			@wraps(f)
			def inner(*args,**kwargs):
				if args[1] :
					if verify_reg(args[0]) :
						#If the document exists already, then we can't insert.
						return False
					else :
						args[0].set_admin(True)
				f(*args)
			return inner
		else:
			@wraps(f)
			def inner(*args,**kwargs):
				if args[1] :
					if verify_reg(args[0]) :						
						return False
				f(*args)
			return inner
	return decorate
def update_user(check=""):
	@restricted(check)
	def update(user,insert=False):
		print "update"
		D = user.jsonify()

		if insert : 
			users.insert(D)
		else :
			users.update(
				{ 'username' : user.username },
				{'$set' : D}
			)
			
	return update

def verify_user(check=""):
	def verify(user):
		if check=="admin" :
			if users.find({"username":user.username,"admin":True}).count()>=1 :
				return True
		else:
			if users.find({"username":user.username}).count()>=1 :
				return True
		return False
	return verify

update_admin = update_user("admin")
update_reg = update_user("")
verify_admin = verify_user("admin")
verify_reg = verify_user("")




D={"password":"durr"}
derp = User("swagger",D)

update_admin(derp,True)







 
