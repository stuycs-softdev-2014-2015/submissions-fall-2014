import unittest

def validate_password_length(pword):
    return len(pword) >= 6 and len(pword) <= 8

def validate_password_has_number(pword):
    for x in pword:
        if(x.isdigit()):
            return True
    return False

def validate_password_has_upper(pword):
    for x in pword:
        if(x.isupper()):
            return True
    return False

def validate_password_has_lower(pword):
    for x in pword:
        if(x.islower()):
            return True
    return False
def validate_email(email):
    has_alpha=False
    has_a=False
    has_alpha2=False
    has_dot=False
    for x in email:
        if(not(has_alpha) and x.isalpha()):
            has_alpha=True
            continue
        if(has_alpha and x=="@"):
            has_a=True
            continue
        if(has_a and x.isalpha()):
            has_alpha2=True
            continue
        if(has_alpha2 and x=="."):
            has_dot=True
            continue
        if(has_dot and x.isalpha()):
            return True
    return False
def validate_phone_number(num):
    if(len(num)!=12):
        return False
    dash= num[3]=="-" and num[6]=="-"
    numbers=True
    for x in num[0:3]+num[4:6]+num[6:]:
        numbers = numbers and x.isdigit()
    return dash and numbers
    
class UtilsTest(unittest.TestCase):
    def __init__(self):
        
    def m1(self):
        pass
    def m2(self):
        pass
    
