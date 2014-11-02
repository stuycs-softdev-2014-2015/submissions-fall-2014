import random
from pymongo import Connection

def setup():
	conn = Connection()
	db = conn['jsdt']
	db.jsdt.drop()
		
	users = {'thluffy':0001,'dennis':0002,'bucky':0003,'doughjoe':0004}

	dlist = []
	for i in users:
		d = {'name':i,'pw':users[i]}
		dlist.append(d)

	db.jsdt.insert(dlist)
	print "COLLECTION"
	print(db.collection_names())
	print "FIND"
	res = db.jsdt.find({})
	info = [x for x in res]
	print info

if __name__ == '__main__':
	setup()