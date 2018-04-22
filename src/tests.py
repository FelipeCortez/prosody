import unittest
from sampa_mbrola import *


class TestConversions(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def testPhonemeConversion(self):
        self.assertEqual(self.converter.convert_phoneme("u~bigo")[0], "um")
        self.assertEqual(self.converter.convert_phoneme("sala")[0], "s")
        # casca


class TestMisc(unittest.TestCase):
    def testFlatten(self):
        self.assertEqual(flatten([[50, 150], [70, 130]]),
                         [50, 150, 70, 130])


if __name__ == '__main__':
    unittest.main()
