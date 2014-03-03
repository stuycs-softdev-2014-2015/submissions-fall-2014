from pymongo import MongoClient
from time import strftime
from bson.objectid import ObjectId
import random

def auth (user, passwd, coll):
    return [x for x in coll.find({'username': user, 'password': passwd})] != []

def addUser (user, passwd, coll):
    coll.insert({'username': user, 'password': passwd})

def addPost (user, title, genre, text, coll):
    coll.insert({'username': user, 'date': strftime("%Y-%M-%d %H:%M:%S"), 'title': title, 'genre': genre, 'text': text, 'comments': []})

def getPosts (user, coll):
    return [x for x in coll.find({'username':user}).sort([('date',-1)])]

def getPostsGenre(genre, coll):
    return [x for x in coll.find({'genre':genre}).sort([('date',-1)])]

def getPost(_id, coll):
    return [x for x in coll.find({'_id':ObjectId(_id)})]

def getRandPost(coll):
    r = [x for x in coll.find()]
    return r[int(random.random() * coll.count())]

def addComment(_id, user, text, coll):
    comments = getPost(_id, coll)[0]['comments'];
    comments.insert(0,[user,text])
    coll.update({'_id':ObjectId(_id)},{'$set': {'comments':comments}})

def getComments(_id, coll):
    l = getPost (_id, coll)[0].comments
    l.reverse()
    return l
