import unittest

import dictionary


class TestDictionary(unittest.TestCase):
    def test1(self):
        self.assertEqual(dictionary.retrive_definition("ok"), ['Colloquial expression of acceptance.'], "False")

    def test2(self):
        self.assertEqual(dictionary.retrive_definition("hello"), ['Expression of greeting used by two or '
                                                                  'more people who meet each other.'], "False")


if __name__ == "__main__":
    unittest.main()
