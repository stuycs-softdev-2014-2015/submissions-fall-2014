import unittest
import filterName


class TestRegexFunctions(unittest.TestCase):
    def setUp(self):
        self.testString = "Hello this is a test String made by Eric Chen"

    def testNameSearch(self):
        names = filterName.getNames(self.testString)
        self.assertIn("Eric Chen", names)

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRegexFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)

