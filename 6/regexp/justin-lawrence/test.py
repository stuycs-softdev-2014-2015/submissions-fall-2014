import unittest

import namere


class TestNameRegex(unittest.TestCase):
    def test_two_name(self):
        corpus = "Lorem ipsum dolor sit amet Justin Kim"
        names = namere.find_names(corpus)
        assert "Justin Kim" in names

    def test_o_apostrophe(self):
        corpus = "Steven O'Malley"
        names = namere.find_names(corpus)
        assert "Steven O'Malley" in names

    def test_mc(self):
        corpus = "Stephen McClellan"
        names = namere.find_names(corpus)
        assert "Stephen McClellan" in names

    def test_three_name(self):
        corpus = "Harrison Parker Chiu"
        names = namere.find_names(corpus)
        assert "Harrison Parker Chiu" in names

if __name__ == '__main__':
        unittest.main()