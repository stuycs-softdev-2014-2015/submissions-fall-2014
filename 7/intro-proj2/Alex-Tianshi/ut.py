import unittest

def validate_number(num):
    l = len(num)
    if l != 10:
        return False
    else:
        for c in num:
            if c not in "1234567890":
                return False
    return True

def validate_email(email):
    return "@" in email and "." in email

def validate_password(pword):
    l = len(pword)
    if l<6 or l>8:
        return False
    else:
        return True

class TestDemo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_shortnum(self):
        r = validate_number("123")
        self.assertEqual(r,False)
    def test_longnum(self):
        r = validate_number("1234567890123")
        self.assertEqual(r,False)
    def test_goodlengthnum(self):
        r = validate_number("1234567890")
        self.assertEqual(r,True)
    def test_notnums(self):
        r = validate_number("12345a7890")
        self.assertEqual(r,False)
    def test_goodemail(self):
        r = validate_email("z@stuycs.org")
        self.assertEqual(r, True)
    def test_period(self):
        r = validate_email("z@stuycscom")
        self.assertEqual(r,False)
    def test_at(self):
        r = validate_email("zstuycs.com")
        self.assertEqual(r,False)
    def test_shortpw(self):
        r = validate_password("123")
        self.assertEqual(r,False)
    def test_longpw(self):
        r = validate_password("1234567890")
        self.assertEqual(r,False)
    def test_goodlengthpw(self):
        r = validate_password("123456")
        self.assertEqual(r,True)
        
    
if __name__=="__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
