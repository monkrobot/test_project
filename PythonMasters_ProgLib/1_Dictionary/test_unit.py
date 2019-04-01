import unittest

import dictionary


class DictTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(dictionary.retrive_definition("ok"), ['Colloquial expression of //acceptance.'],
                         "Failed test1 in test_unit.py")

if __name__ == "__main__":
    unittest.main()
