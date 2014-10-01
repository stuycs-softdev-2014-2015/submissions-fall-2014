#Angela Lin and Christina Ko
#Uniitest Practice

import unittest

#valid email must have an '@' and a '.'
def validate_email(email):
    if email.find("@") == -1 or email.find(".") == -1: #not in email
        return False
    else:
        return True

#length of a valid phone number must be 10 and all chars must be numbers
def validate_phone(phone):
    p = len(phone)
    for a in phone:
        if ord(a) < ord('0') or ord(a) > ord('9'):
            return False
    return (p==10)

#valid password must be 6-8 chars in length, have at least one uppercase letter, lowercase letter, and num
def validate_pword(pword):
    if len(pword) < 6 or len(pword) > 8:
        return False
    elif not findUpper(pword) or not findLower(pword) or not findNumber(pword):
        return False
    else:
        return True

#helper fxn to search for uppercase letter
def findUpper(word):
    for a in word:
        if ord(a) >= ord('A') and ord(a) <= ord('Z'):
            return True
    return False

#helper fxn to search for lowercase letter
def findLower(word):
    for a in word:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            return True
    return False

#helper fxn to search for number
def findNumber(s):
    for a in s:
        if ord(a) >= ord('0') and ord(a) <= ord('9'):
            return True
    return False

#=======================================================
#=======================================================

class TestDemo(unittest.TestCase):
    def setUp(self):
        pass #placeholder

    def tearDown(self):
        pass #placeholder

#=======================================================        
#EMAIL VALIDATION

    #case when email is missing an '@'
    def test_at(self):
        r = validate_email("christinakgmail.com")
        self.assertEqual(r, False)

    #case when email is missing an '.'
    def test_period(self):
        r= validate_email("angelal@gmailcom")
        self.assertEqual(r, False)

    #GOOD EMAIL ADDRESS
    def test_goodemail(self):
        r = validate_email("christinaangelaswag@gmail.com")
        self.assertEqual(r, True)

#=======================================================
#PHONE NUMBER VALIDATION:

    #case when phone number is ten digits long
    def test_ten(self):
        r=validate_phone("1234567890")
        self.assertEqual(r,True)
    
    #case when phone number is longer than ten digits    
    def test_plong(self):
        r=validate_phone("1234576028395673")
        self.assertEqual(r,False)
        
    #case when phone number is shorter than ten digits
    def test_pshort(self):
        r=validate_phone("123")
        self.assertEqual(r,False)

    #case when not all ten chars are digits
    def test_all_num(self):
        r=validate_phone("12abcdefgo")
        self.assertEqual(r,False)

    #GOOD PHONE NUMBER
    def test_good_phone(self):
        r=validate_phone("7181234567")
        self.assertEqual(r,True)
        
#=======================================================        
#PASSWORD VALIDATION:

    #case when missing uppercase letter
    def test_Upper(self):
        r=validate_pword("aei2134")
        self.assertEqual(r,False)

    #case when missing lowercase letter
    def test_lower(self):
        r = validate_pword("ABCD12")
        self.assertEqual(r,False)

    #case when pword is too long
    def test_long(self):
        r=validate_pword("123457980456")
        self.assertEqual(r, False)

    #case when pword is too short
    def test_short(self):
        r = validate_pword("1")
        self.assertEqual(r, False)

    #case when pword is missing a number
    def test_num(self):
        r= validate_pword("asdfg")
        self.assertEqual(r, False)

    #GOOD PWORD:
    def test_pgood(self):
        r = validate_pword("Ac0704")
        self.assertEqual(r, True)
        
#========================================================        
if __name__=="__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
