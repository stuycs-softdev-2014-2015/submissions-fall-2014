import unittest

def validateEmail(email):
    return ("@" in email) and ("." in email)

def validatePhone(phone):
    for char in phone:
        if char in " -()":
            phone = phone.replace(char,'')
    return len(phone) == 10

def validatePassword(pword):
    return len(pword) >= 6 and len(pword) <= 8 and hasUpper(pword) and hasLower(pword) and hasNumber(pword)

def hasUpper(pword):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in pword:
        if i in upper:
            return True
    return False

def hasNumber(pword):
    nums = "1234567890"
    for i in pword:
        if i in nums:
            return True
    return False

def hasLower(pword):
    Lower = "abcdefghijklmnopqrstuvwxyz"
    for i in pword:
        if i in Lower:
            return True
    return False


class TestDemo(unittest.TestCase):
    def test_short(self):
        r = validatePassword("123")
        self.assertEqual(r,False)
    def test_long(self):
        r = validatePassword("1234567890")
        self.assertEqual(r,False)
        
    def test_goodlength(self):
        r = validatePassword("12gD567")
        self.assertEqual(r,True)

    def test_noAt(self):
        r = validateEmail("andreasdline.com")
        self.assertEqual(r,False)

    
    def test_noDot(self):
        r = validateEmail("andreas@dlinecom")
        self.assertEqual(r,False)

                
    def test_goodEmail(self):
        r = validateEmail("andreas@dline.com")
        self.assertEqual(r,True)


    def test_goodPhone(self):
        r = validatePhone("1234567890")
        self.assertEqual(r,True)

        
    def test_greatPhone(self):
        r = validatePhone("(123) 456-7890")
        self.assertEqual(r,True)

        
    def test_shortPhone(self):
        r = validatePhone("123456789")
        self.assertEqual(r,False)

        
    def test_longPhone(self):
        r = validatePhone("12345678901")
        self.assertEqual(r,False)


        
if __name__=="__main__":
#unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
