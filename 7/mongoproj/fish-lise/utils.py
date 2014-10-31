d = {}
def authenticate(uname,pword):
    try:
        return d[uname]==pword;
    except:  #if error occurs if uname not in d
        return False



def adduser(uname,pword):
    if uname not in d:
        d[uname]= pword
        return True
    else:
        return False
