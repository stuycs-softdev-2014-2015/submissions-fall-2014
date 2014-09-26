import unittest

def validate_email(email):
    at = str.find(email, "@")
    period = str.find(email, ".")
    if (at <= 0) or (period <= 0) or (at >= len(email)-5) or (period >= len(email) - 3):
        return False
    else:
        return True

def validate_phone(phone):
    if (len(phone) == 10):
        return True
    else:
        return False

def validate_password(password):
    if (len(password) < 6) or (len(password) > 8) or (upper(password) == False) or (lower(password) == False) or (digit(password) == False):
        return False
    else:
        return True

def upper(password):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for p in password:
        if (str.find(uppers, p) >= 0):
            return True
    return False

def lower(password):
    lowers = "abcdefghijklmnopqrstuvwxyz"
    for p in password:
        if (str.find(lowers, p) >= 0):
            return True
    return False

def digit(password):
    digits = "1234567890"
    for p in password:
        if (str.find(digits, p) >= 0):
            return True
    return False


class TestDemo(unittest.TestCase):
    def test_email_work(self):
        r = validate_email("coby.goldberg@gmail.com")
        if r == True:
            print "Coby's email passed"
        else:
            print "Coby's email failed"
    
    def test_at(self):
        r = validate_email("coby.goldberg.com")
        if r == True:
            print "No at, passed"
        else:
            print "No at, failed"

    def test_dot(self):
        r = validate_email("coby.goldberg@")
        if r == True:
            print "No website passed"
        else:
            print "No website failed"

    def test_toolong(self):
        r = validate_phone("1234567890123476677877655423423234234655612")
        if r == True:
            print "too long phone passed"
        else:
            print "too long phone failed"

    def test_correctphone(self):
        r = validate_phone("1234567890")
        if r == True:
            print "correct length phone passed"
        else:
            print "correct length phone failed"

    def test_tooshort(self):
        r = validate_phone("167890")
        if r == True:
            print "too short phone passed"
        else:
            print "too short phone failed"

    def test_nonumber(self):
        r = validate_password("cobyLev")
        if r == True:
            print "no number in password, passed"
        else:
            print "no number in password, failed"

    def test_noupper(self):
        r = validate_password("cobylev1")
        if r == True:
            print "no uppercase in password, passed"
        else:
            print "no uppercase in password, failed"
       
    def test_nolower(self):
        r = validate_password("COBYLEV1")
        if r == True:
            print "no lowercase in password, passed"
        else:
            print "no lowercase in password, failed"
        
    def test_toolongpassword(self):
        r = validate_password("cobyLevLE455456")
        if r == True:
            print "too long password, passed"
        else:
            print "too long password, failed"

    def test_tooshortpassword(self):
        r = validate_password("cL1")
        if r == True:
            print "too short password, passed"
        else:
            print "too short password, failed"

    def test_correctpassword(self):
        r = validate_password("cobyLev1")
        if r == True:
            print "correct password, passed"
        else:
            print "correct password, failed"

if __name__=="__main__":
#unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
