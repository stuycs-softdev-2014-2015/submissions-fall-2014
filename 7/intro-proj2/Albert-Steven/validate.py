import unittest

def validate_email(e):
    for c in e:
        if (c == '@'):
            return True
    return False

def validate_phone(p):
    return len(str(p))==10

def validate_password(p):
    upper = False
    lower = False
    digit = False
    if (len(p) >= 6 and len(p) <= 8):
        for c in p:
            if (c >= 'A' and c <= 'Z'):
                upper = True
            if (c >= 'a' and c <= 'z'):
                lower = True
            if (c >= '0' and c <= '9'):
                digit = True
    return (upper and lower and digit)

#====================================================================
    
class validate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    
    def test_email_wrong(self):
        r = validate_email("blah")
        self.assertEqual(r,False)

    def test_email_right(self):
        r = validate_email("blah@blah.com")
        self.assertEqual(r,True)


               
    def test_phone_long(self):
        r = validate_phone(1234567890123456)
        self.assertEqual(r,False)

    def test_phone_short(self):
        r = validate_phone(123)
        self.assertEqual(r,False)

    def test_phone_right(self):
        r = validate_phone(1234567890)
        self.assertEqual(r,True)

        
                
    def test_pw_short(self):
        r = validate_password("sW2")
        self.assertEqual(r,False)

    def test_pw_long(self):
        r = validate_password("Swagaron10")
        self.assertEqual(r,False)

    def test_pw_noupper(self):
        r = validate_password("asfghie3")
        self.assertEqual(r,False)

    def test_pw_nolower(self):
        r = validate_password("SWAGLOL7")
        self.assertEqual(r,False)      

    def test_pw_nodigit(self):
        r = validate_password("caRrots")
        self.assertEqual(r,False)

    def test_pw_right(self):
        r = validate_password("Passw0rd")
        self.assertEqual(r,True)      

#====================================================================
                
if __name__=="__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(validate)
    unittest.TextTestRunner(verbosity=2).run(suite)
