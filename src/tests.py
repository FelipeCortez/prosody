import unittest


class TestConversions(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def testPhonemeConversion(self):
        self.assertEqual(self.converter.convert_phoneme("u~bigo"), "um")

if __name__ == '__main__':
    unittest.main()
