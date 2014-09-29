import unittest

def valid_password(pword):
    validlen = len(pword) <= 8 and len(pword) >= 6
    validcase = (pword.upper() != pword) and (pword.lower() != pword)
    validnum = False
    for num in range(10):
        validnum = validnum or (str(num) in pword)
    return validlen and validnum and validcase
        
def valid_email(email):
    return "." in email and "@" in email

def valid_phone(phone):
    return len(phone) == 10

class TestParameters(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_short(self):
        r = valid_password("1Ab")
        self.assertEqual(r,False)
    def test_long(self):
        r = valid_password("12345678cD")
        self.assertEqual(r,False)
    def test_noupper(self):
        r = valid_password("apple1")
        self.assertEqual(r,False)
    def test_nolower(self):
        r = valid_password("APPLE2")
        self.assertEqual(r,False)
    def test_nonumber(self):
        r = valid_password("BaNaNa")
        self.assertEqual(r,False)
    def testpw_valid(self):
        r = valid_password("ItW0rks")
        self.assertEqual(r,True)
    def test_noat(self):
        r = valid_email("stuy.com")
        self.assertEqual(r,False)
    def test_nodot(self):
        r = valid_email("stuy@com")
        self.assertEqual(r,False)
    def testemail_valid(self):
        r = valid_email("StuyStudent@stuy.com")
        self.assertEqual(r,True)
    def testnum_invalid(self):
        r = valid_phone("1244434567890")
        self.assertEqual(r, False)
    def testnum_valid(self):
        r = valid_phone("1234567890")
        self.assertEqual(r, True)
        
if __name__=="__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParameters)
    unittest.TextTestRunner(verbosity=2).run(suite)
