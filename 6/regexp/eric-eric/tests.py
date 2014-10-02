import unittest
import filterName


class TestRegexFunctions(unittest.TestCase):
    def setUp(self):
        self.testString = "Hello this is a test String made by Eric Chen"
        self.testString2 = "Brian O'Malley"
        self.testString3 = "Brian O-Malley"
        self.testStringMultipleNames = "Brian O'Malley said hi to Eric Chen"
        self.testStringSurnames = "Mr. Smith is a test person"

    def testNameSearchSimpleSurnames(self):
        """should not match to a name such as Mr. Smith"""
        names = filterName.getNames(self.testStringSurnames)
        self.assertNotIn("Smith", names)

    def testNameSearchSimple(self):
        names = filterName.getNames(self.testString)
        self.assertIn("Eric Chen", names)

    def testNameSearchApostrophe(self):
        names = filterName.getNames(self.testString2)
        self.assertIn("Brian O'Malley", names)

    def testNameSearchHyphen(self):
        names = filterName.getNames(self.testString3)
        self.assertIn("Brian O-Malley", names)

    def testNameSearchSurnamesSimple(self):
        """should not match normal names such as Eric Chen"""
        names = filterName.getSurnames(self.testString)
        self.assertNotIn("Smith", names)

    def testNameSearchSurnames(self):
        names = filterName.getSurnames(self.testStringSurnames)
        self.assertIn("Smith", names)


class TestCleaningFunctions(unittest.TestCase):
    def setUp(self):
        self.exampleNames = ["Eric Chen", "Brian O'Malley", "Another Name"]
        self.testString = """Eric Chen Eric Chen Eric Chen
        Brian O'Malley Brian O'Malley Brian O'Malley
        Another Name Another Name Another Name
        """

    def testRemoveDuplicates(self):
        names = filterName.getNames(self.testString)
        D = filterName.deleteDuplicates(names)
        namecount = True

        for name in self.exampleNames:
            if D[name] != 3:
                namecount = False

        self.assertEqual(namecount, True)

    def testSplitName(self):
        names = filterName.splitName(self.exampleNames)
        self.assertIn("Eric", names)
        self.assertIn("Chen", names)
        self.assertIn("Brian", names)
        self.assertIn("O'Malley", names)
        self.assertIn("Another", names)
        self.assertIn("Name", names)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRegexFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCleaningFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
