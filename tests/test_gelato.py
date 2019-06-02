import unittest

from calc.gelato import Gelato

class TestGelato(unittest.TestCase):

    def test_class_exists(self):
        self.assertTrue(Gelato())

if __name__ == '__main__':
    unittest.main()