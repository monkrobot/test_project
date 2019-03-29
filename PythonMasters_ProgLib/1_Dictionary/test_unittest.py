import unittest
import dictionary


class TestDictionary(unittest.TestCase):
    def test1(self):
        self.assertEqual(dictionary.retrive_definition("word"), "A distinct unit of language(sounds " \
                                                        "in speech or written letters) with a particular meaning, " \
                                                        "composed of one or more morphemes, and also of one or more " \
                                                        "phonemes that determine its sound pattern.", "False")

    def test2(self):
        self.assertEqual(dictionary.retrive_definition("nato"), "An international organization created in 1949 by " \
                                                                "the North Atlantic Treaty for purposes of collective " \
                                                                "security.", "False")


if __name__ == "__main__":
    unittest.main()
