import unittest

from calc.gelato import Gelato

class TestGelato(unittest.TestCase):

    def test_class_exists(self):
        self.assertTrue(Gelato())

    def test_ingredients_list(self):
        g = Gelato()
        self.assertEqual(g.ingredients, [])

if __name__ == '__main__':
    unittest.main()