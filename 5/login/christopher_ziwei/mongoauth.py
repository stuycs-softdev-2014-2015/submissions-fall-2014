from pymongo import MongoClient

def add(user, password):
  conn = MongoClient()
  db = conn['userdatabase']
  if (notvalid(user) or notvalid(password)) and db.database.find({'username' : user}).count() == 0:
    db.database.insert({'username': user , 'password': password})
    return True
  return False  
    
def verify(user, password):
  conn = MongoClient()
  db = conn['userdatabase']
  return db.database.find({'username': user , 'password': password}).count() == 1
  
def notvalid(string):
  return len([filter(lambda x: x in "+=\\#[]{}()'\"", string)]) > 0
