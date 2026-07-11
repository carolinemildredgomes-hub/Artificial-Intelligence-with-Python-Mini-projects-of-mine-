"""
Dictionary tests.
"""

import unittest

from src.dictionary import Dictionary


class TestDictionary(unittest.TestCase):

    def setUp(self):

        self.dictionary = Dictionary()


    def test_valid_word(self):

        self.assertTrue(
            self.dictionary.is_word(
                "HELLO"
            )
        )


    def test_invalid_word(self):

        self.assertFalse(
            self.dictionary.is_word(
                "XYZABC"
            )
        )


if __name__ == "__main__":
    unittest.main()
