import unittest

from translator import  english_to_french,french_to_english

class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("dad"),"Papa")
        self.assertEqual(english_to_french(""), "")

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("papa"),"Dad")
        self.assertEqual(french_to_english(""),"")

if __name__ == '__main__':
    unittest.main()