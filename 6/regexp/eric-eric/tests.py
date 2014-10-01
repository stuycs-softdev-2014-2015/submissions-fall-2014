import unittest
import filterName


class TestRegexFunctions(unittest.TestCase):
    def setUp(self):
        self.testString = "Hello this is a test String made by Eric Chen"

    def testNameSearch(self):
        names = filterName.getNames(self.testString)
        assertIn("Eric Chen", names)
