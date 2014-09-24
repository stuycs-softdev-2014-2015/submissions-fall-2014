class EmailValidator(unittest.testCase)

#Incorrect Emails
    def test_empty(self):
        r = validate_email("")
        r.assertEqual(r, false)
    def test_empty_user(self):
        r = validate_email("@gmail.com")
        r.assertEqual(r, false)
    def test_empty_domain(self):
        r = validate_email("genjinoguchi")
        r.assertEqual(r, false)
    def test_empty(self):
        r = validate_email("genjinoguchigmail.com")
        r.assertEqual(r, false)
    def test_no_domain(self):
        r = validate_email("genjinoguchi")
        r.assertEqual(r, false)
    def test_if_user_space(self):
        r = validate_email("genji noguchi@gmail.com")
        r.assertEqual(r, false)
    def test_if_domain_space(self):
        r = validate_email("genji noguchi@gm ail.com")
        r.assertEqual(r, false)
    def test_no_domain_period(self):
        r = validate_email("genjinoguchi@g")
        r.assertEqual(r, false)
    def test_bad_domain(self):
        r = validate_email("genji@noguchig.com")
        r.assertEqual(r, false)

#Correct Emails:
    def test_normal(self):
        r = validate_email("genjinoguchi@gmail.com")
        r.assertEqual(r, true)
    def test_user_period(self):
        r = validate_email("genji.noguchi@gmail.com")
        r.assertEqual(r, true)
    def test_domain_two_periods(self):
        r = validate_email("genji@bart.stuy.edu")
        r.assertEqual(r, false
