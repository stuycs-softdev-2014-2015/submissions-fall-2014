import pymongo


conn = pymongo.MongoClient()
db = conn.userDatabase


def checkLogin(uName, pword):
    return True

    # if(db.userData.find({'userName': uName, 'password': pword}).count() == 0):
    #     return False;
    # else:
    #     return True;
    #     
