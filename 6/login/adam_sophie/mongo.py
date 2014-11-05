import pymongo, csv
from pymongo import Connection


conn = Connection()
db = conn["uncommon"]
users = db.users
colleges = db.colleges

def new_user(udict):
    pwcheck = (udict['pw'] == udict['rpw'])
    uname = udict['uname'] 
    uncheck = users.find_one({'uname':uname}) == None
    s = ""
    if uncheck == False:
        s = "That username has already been used"
    elif not (len(udict['pw']) >= 5 and len(udict['pw']) <= 20):
        s= "Password must be between 5 and 20 characters"
    elif pwcheck == False:
        s =  "Passwords do not match"
    else:
        addperson(udict)
    print s
    return s

def check_pword(uname,pw):
    rpw = getAttribute(uname,"pw")
    if rpw == None:
        return "Username does not exist"
    if rpw == pw:
        return ""
    else:
        return "Wrong password"

def addperson(pdict):
    pdict['colleges'] = []
    users.insert(pdict)
    

def addfield(uname, field, data):
    #p = users.find_one({"fname":fname})
    #p[field] = data
    #users.save(p)
    users.update({"uname":uname},{'$set':{field:data}})

def addColleges(uname, cols):
    p = users.find_one({'uname':uname})
    for c in cols:
        p['colleges'].append(c)
    users.save(p)
    
def getAttribute(uname, field):
    ret = users.find_one({'uname':uname, field:{'$exists':True}})
    if ret == None:
        return None
    ret = ret.get(field)
    #print(ret)
    return ret

def getUser(uname):
    return users.find_one({'uname':uname})
    
def createColleges():
    cols = csv.DictReader(open("colleges.csv"))
    for c in cols:
        c['min gpa'] = int(c['min gpa'])
        colleges.insert(c)

def collegeLookup(uname, d):
    ucols = getAttribute(uname, 'colleges')
    colnames = []
    if d.has_key('min gpa'):
        d['min gpa'] = {'$gte': int(d['min gpa'])} 
    for c in colleges.find(d):
        if c['name'] not in ucols:  
            colnames.append(colleges.find_one({'name':c['name']}))
    return colnames

def getColleges():
    return colleges.find()


if __name__ == '__main__':
    #users.remove() #----AFTER YOU RUN THIS COMMENT THIS OUT-----#
    colleges.remove()    
    createColleges()
    
    peeps = collegeLookup('sophgersh',{'min gpa':100})

    """
    peeps = users.find({},{'_id':False}) 
    for p in peeps:
        print p
   
    print "PEOPLE"     
    peeps = users.find({},{'_id':False}) 
    for p in peeps:
        print p
        
  
    d = {}
    d['size'] = 'medium'
    d['type'] = 'private'
    d['location'] = 'Boston'
    d['min gpa'] = '100'
    cols = collegeLookup(d)
    
    for c in cols:
        print c
    """
    
        
"""
 people = db.people
 
 to insert
     people.insert(dict)
        
 to update:
     person = people.find_one({"food":"ham","name":"sophie"})
     person["food"] = "eggs"
     people.save(person)

 to remove:
     for person in people.find():
        people.remove(person)

 people.find(dict) --> returns a list of people with the dict qualities
 users.remove({"fname":{"$exists":False}})
"""

    
