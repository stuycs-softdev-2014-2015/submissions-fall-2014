from flask import Flask
from flask import session, url_for, request, redirect, render_template
from pymongo import MongoClient

def work():
    client = MongoClient()
    try:
        db = client["account"]
    except:
        pass
    return db


def register(username,password,security,answer):
    db = work()
    chk = db.account.find_one({'username':username})
    print chk
    if(chk == None):
       db.account.insert({'username':username,'password':password,'security':security,'answer':answer})
       return True
    else:
        return False
   

def authenticate(username,password):
    db = work()
    user = [x for x in db.account.find({'username':username,'password':password},fields={'_id':False})]
    if (len(user) == 0):
        return False
    user =  user[0]
    if username == user['username'] and password == user['password']:
        return True
    else:
        return False


def change(username,newpassword):
    db = work()
    db.account.update({'username':username},{'$set':{'password':newpassword}})
    return True



def recover(username,security,answer):
    db = work()
    user = [x for x in db.account.find({'username':username},fields={'_id':False})]
    user = user[0]
    if(answer == user['answer'] and security == user['security']):
        return ("Your password is: " + user['password'])
    else:
        return ("Your username and security answer do not match. Please try again.")