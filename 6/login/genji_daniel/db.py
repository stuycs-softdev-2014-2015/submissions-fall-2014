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
	def set_username(self,username):
		self.username=username
	def set_password(self,password):
		self.password=password
	def jsonify(self):
		D = {}

		D['username']=self.username
		
		if self.password:
			D['password']=self.password		
		else:
			print "This should never fail, because there are prior password checks."

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
						args[0]["admin":True]
				f(*args)
			return inner
		else:
			@wraps(f)
			def inner(*args,**kwargs):
				print f.__name__
				if args[1] :
					if verify_reg(args[0]) :
						return False
				f(*args)
			return inner
	return decorate
def update_user(check=""):
	@restricted(check)
	def update(user,insert=False):
		print "screw you python"	
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
			if users.find({"username":user.username})>=1 :
				return True
		return False

update_admin = update_user("admin")
update_reg = update_user("")
verify_admin = verify_user("admin")
verify_reg = update_user("")

D={"password":"durr"}
derp = User("swagmaster",D)

update_reg(derp,True)







 
