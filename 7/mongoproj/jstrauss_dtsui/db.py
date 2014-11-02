# Justin Strauss and Derek Tsui
# Software Development Period 7
# MongoDB Project

import random, re
from pymongo import Connection

def setup():
	conn = Connection()
	db = conn['jsdt']
	db.jsdt.drop()
		
	# user = {'thluffy':0001,'dennis':0002,'bucky':0003,'doughjoe':0004}
	users = [["justin","jis7991@gmail.com","test"],["derek","dtsui918@yahoo.com","test"],["zamansky","zamansky@stuycs.org","test"]]

	dlist = []
	for i in range(len(users)):
		d = {'name':users[i][0],'email':users[i][1],'pw':users[i][2]}
		dlist.append(d)

	db.jsdt.insert(dlist)

	# print "COLLECTION"
	# print(db.collection_names())
	# print "FIND"
	# res = db.jsdt.find({},{"_id":False})
	# info = [x for x in res]
	# print info

def authenticate(username,password):
	conn = Connection()
	db = conn['jsdt']
	return 1 == (db.jsdt.find({'name':username,'pw':password})).count()

def userexists(username):
	conn = Connection()
	db = conn['jsdt']
	return 1 == (db.jsdt.find({'name':username})).count()

def emailexists(email):
	conn = Connection()
	db = conn['jsdt']
	return 1 == (db.jsdt.find({'email':email})).count()

def getcontacts(username):
	conn = Connection()
	db = conn['jsdt']
	res = db.jsdt.find({'name':{'$not':re.compile(username)}},{"_id":False})
	info = [x for x in res]
	return info

def getprofile(username):
	conn = Connection()
	db = conn['jsdt']
	res = db.jsdt.find({'name':username},{"_id":False})
	info = [x for x in res]
	return info

def updatepw(username,newpw):
	conn = Connection()
	db = conn['jsdt']
	db.jsdt.update({'name':username},{'$set':{'pw':newpw}})

def adduser(username,email,password):
	conn = Connection()
	db = conn['jsdt']
	db.jsdt.insert([{'name':username,'email':email,'pw':password}])

# if __name__ == '__main__':
# 	setup()