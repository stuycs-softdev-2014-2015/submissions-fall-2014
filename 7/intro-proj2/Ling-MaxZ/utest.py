import unittest
import re

def validate_password(pword):
    l = len(pword)
    if l<6 or l>8:
        return False
    else:
        return True

class TestPassword(unittest.TestCase):
    #def setUp(self):
        #print 'init'
    #def tearDown(self):
        #print 'cleanup'
    def test_short(self):
        r = validate_password("123")
        self.assertEqual(r,False)
    def test_long(self):
        r = validate_password("1234567890")
        self.assertEqual(r,False)
    def test_goodlength(self):
        r = validate_password("123456")
        self.assertEqual(r,True)

def validate_phone(phone):
    l = len(phone)
    #US country code works yes
    if l>11 or l<10:
        return False
    matches = re.search(r'[^0-9a-zA-Z]', phone)
    if matches != None:
        return False
    else:
        return True
    
        
class TestPhone(unittest.TestCase):
    def test_short(self):
        r = validate_phone("1")
        self.assertEqual(r, False)
    def test_long(self):
        r = validate_phone("1047823759237489235892374892374")
        self.assertEqual(r, False)
    def test_goodlength(self):
        r = validate_phone("1234567890")
        self.assertEqual(r, True)
    def test_goodnumber(self):
        r = validate_phone("123456789a")
        self.assertEqual(r, True)
    def test_badnumber(self):
        r = validate_phone("!@#$%^&*()")
        self.assertEqual(r, False)

def validate_email(email):
    matches = re.search(r'^.*\@.+\..+', email)
    return matches != None
        
class TestEmail(unittest.TestCase):
    def test_at(self):
        r = validate_email("werjhiueiwj.com")
        self.assertEqual(r, False)
    def test_dot(self):
        r = validate_email("fjkakdfoasi@ksadkod")
        self.assertEqual(r, False)
    def test_short(self):
        r = validate_email("a@a.")
        self.assertEqual(r, False)
    def test_okay(self):
        r = validate_email("jdai315@gmail.com")
        self.assertEqual(r, True)
        
        

if __name__=="__main__":
    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestPassword)
    unittest.TextTestRunner(verbosity=2).run(suite1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestPhone)
    unittest.TextTestRunner(verbosity=2).run(suite2)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestEmail)
    unittest.TextTestRunner(verbosity=2).run(suite3)



        
