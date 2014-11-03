from pymongo import MongoClient

client = MongoClient()
db = client.account_manager

sessions = db.sessions

def insert(username, session_id):
    if (not user_exists(username)):
        new_user = {
                "username" : username,
                "session_id" : session_id
                }
        sessions.insert(new_user)
    else:
        print "User exists."

def user_exists(username):
    return sessions.find({"username" : username}).count() > 0

def remove(username):
    sessions.remove({"username" : username})

def validate_session(username, session_id):
    return sessions.find({"username" : username, "session_id" : session_id}).count() > 0

if __name__ == "__main__":
    insert("admin", "f3#@!39018fdp__Ewqe823")
    print "True: " + str(validate_session("admin", "f3#@!39018fdp__Ewqe823"))
    print "False: " + str(validate_session("admin", "f3#@!39018fdp__Ewqe82"))
    remove("admin")



