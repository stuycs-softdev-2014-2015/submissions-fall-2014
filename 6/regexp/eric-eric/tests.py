import unittest
import filterName


class TestRegexFunctions(unittest.TestCase):
    def setUp(self):
        self.testString = "Hello this is a test String made by Eric Chen"
        self.testString2 = "Brian O'Malley"
        self.testStringMultipleNames = "Brian O'Malley said hi to Eric Chen"

    def testNameSearchSimple(self):
        names = filterName.getNames(self.testString)
        self.assertIn("Eric Chen", names)

    def testNameSearchApostrophe(self):
        names = filterName.getNames(self.testString2)
        self.assertIn("Brian O'Malley", names)


class TestCleaningFunctions(unittest.TestCase):
    def setUp(self):
        self.exampleNames = ["Eric Chen", "Brian O'Malley", "Another Name"]
        self.testString = """Eric Chen Eric Chen Eric Chen Eric Chen
        Brian O'Malley Brian O'Malley
        Another Name Another Name Another Name
        """

    def testRemoveDuplicates(self):
        names = filterName.getNames(self.testString)
        D = filterName.deleteDuplicates(names)
        namecount = True

        for name in self.exampleNames:
            if D[name] != 3:
                namecount = false

        self.assertEqual(namecount, True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRegexFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCleaningFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
