import unittest

from calc.gelato import Gelato
from calc.ingredient import Ingredient

class TestGelato(unittest.TestCase):

    def test_class_exists(self):
        self.assertTrue(Gelato())

    def test_ingredients_list(self):
        g = Gelato()
        self.assertEqual(g.ingredients, [])

    def test_add_ingredient(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        i_2 = Ingredient(0, 0, 0, 0, 100, 'Water', 100)
        g.add_ingredient(i_1, i_2)
        self.assertEqual(g.ingredients, [i_1, i_2])

    @unittest.skip
    def test_raise_on_adding_non_ingredient(self):
        g = Gelato()
        with self.assertRaises(TypeError):
            g.add_ingredient(None)

if __name__ == '__main__':
    unittest.main()