import unittest
from sampa_mbrola import *


class TestMisc(unittest.TestCase):
    def testFlatten(self):
        self.assertEqual(flatten([[50, 150], [70, 130]]),
                         [50, 150, 70, 130])


class TestConversions(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def testPhonemeConversion(self):
        self.assertEqual(
            self.converter.convert_sentence("umbigo").mbrola_phones(),
            ["_", "um", "b", "i", "g", "u", "_"])
        self.assertEqual(
            self.converter.convert_sentence("sala").mbrola_phones(),
            ["_", "s", "a", "l", "a", "_"]
        )
        self.assertEqual(
            self.converter.convert_sentence("sírio").mbrola_phones(),
            ["_", "s", "i", "r", "i", "u", "_"]
        )
        self.assertEqual(
            self.converter.convert_sentence("casca").mbrola_phones(),
            ["_", "k", "a", "s2", "k", "a", "_"]
        )

if __name__ == '__main__':
    unittest.main()
