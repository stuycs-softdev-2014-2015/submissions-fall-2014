#Victor Gaitour and David Dvorkin worked on this

import unittest

def validate_email(email):
    for x in email:
        if x == "@":
            for y in email:
                if y == ".":
                    return True
    return False
class TestEmail(unittest.TestCase):
    def test_at(self):
        r=validate_email("blehblehbleh@")
        self.assertEqual(r,False)
    def test_dot(self):
        r=validate_email("blehblehbleh.")
        self.assertEqual(r,False)
    def test_both(self):
        r=validate_email("blehblehblhe@.")
        self.assertEqual(r,True)

    
def validate_phone(phone):
    if len(phone)==10:
        return True
    return False

class TestPhone(unittest.TestCase):
    def test_short(self):
        r=validate_phone("25893")
        self.assertEqual(r,False)
    def test_long(self):
        r=validate_phone("p000000000000000000p")
        self.assertEqual(r,False)
    def test_niccceeee(self):
        r=validate_phone("9786579561")
        self.assertEqual(r,True)

def validate_password(password):
    t1=False
    t2=False
    t3=False
    t4=False
    if len(password)>5 and len(password)<9:
        t1=True
    for x in password:
        if x.islower():
            t2=True
            break
    for x in password:
        if x.isupper():
            t3=True
            break
    for x in password:
        if x.isdigit():
            t4=True
            break
    if t1==True and t2==True and t3==True and t4==True:
         return True
    return False

class TestPassword(unittest.TestCase):
    def test_length(self):
        r = validate_password("Viktorovich1")
        self.assertEqual(r, False)
    def test_lower(self):
        r = validate_password("VIKTOR1")
        self.assertEqual(r, False)
    def test_upper(self):
        r = validate_password("viktor1")
        self.assertEqual(r,False)
    def test_digit(self):
        r = validate_password("Viktor")
        self.assertEqual(r,False)
    def test_gucci(self):
        r = validate_password("Viktor1")
        self.assertEqual(r,True)


    
if __name__=="__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPassword)
    unittest.TextTestRunner(verbosity=2).run(suite)
