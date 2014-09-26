import unittest

def validate_email(email):
    return ("@" in email) and ("." in email)

def validate_phone(phone):
    return len(phone) == 10

def validate_pass(passw):
    b1 = False
    b2 = False
    b3 = False
    for x in passw:
        if x.islower():
            b1 = True
        elif x.isupper():
            b2= True
        if x.isdigit():
            b3 = True
    return len(passw) >= 6 and len(passw) <= 8 and b1 and b2 and b3


class Ineedvalidation(unittest.TestCase):
    def test_email(self):
        self.assertEqual(validate_email("thisisanemail@dumb.com"), True)
        self.assertEqual(validate_email("yolo"), False)
    
    def test_phone(self):
        self.assertEqual(validate_phone("1234567890"), True)
        self.assertEqual(validate_phone("1"), False)
    
    def test_pass(self):
        self.assertEqual(validate_pass("BiffleT3"),True)
        self.assertEqual(validate_pass("Stubbkaneedle"),False)
        self.assertEqual(validate_pass("ttin"),False)
        self.assertEqual(validate_pass("seanlow1"),False)
        self.assertEqual(validate_pass("CNUHEAR1"),False)
        self.assertEqual(validate_pass("6956125"),False)
if (__name__ == "__main__"):
    #unittest.main()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(Ineedvalidation)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    while True:
        s = raw_input('>')
        if s == "Stop":
            break
        print "Email: "+str(validate_email(s))
        print "Phone: "+str(validate_phone(s))
        print "Password: "+str(validate_pass(s))


    
