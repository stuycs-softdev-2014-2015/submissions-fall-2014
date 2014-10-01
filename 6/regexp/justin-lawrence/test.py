import unittest

import namere


class TestNameRegex(unittest.TestCase):
    def test_two_name(self):
        corpus = "Lorem ipsum dolor sit amet Justin Kim"
        names = namere.find_names(corpus)
        assert "Justin Kim" in names

if __name__ == '__main__':
        unittest.main()