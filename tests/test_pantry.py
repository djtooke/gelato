import unittest

from calc.ingredient import Ingredient
from calc.pantry import Pantry

class TestPantry(unittest.TestCase):

    def test_class_exists(self):
        self.assertTrue( Pantry() )

    def test_get_ingredient(self):
        p = Pantry()
        ing = p.get_ingredient('cherries', 150)
        self.assertTrue(isinstance(ing, Ingredient))
        self.assertEqual(ing.sugar, 12)
        self.assertEqual(ing.fat, 0)
        self.assertEqual(ing.lm_s, 0)
        self.assertEqual(ing.oth_s, 8)
        self.assertEqual(ing.water, 80)
        self.assertEqual(ing.dry, 20)
        self.assertEqual(ing.grams, 150)

    def test_invalid_ingredient(self):
        p = Pantry()
        with self.assertRaises(ValueError):
            p.get_ingredient('phlogiston', 150)

    def test_check_ingredient_constituents(self):
        Pantry.store['Kryptonite'] = {'sugar': 100, 'fat': 100, 'lm_s': 100, 'oth_s': 100, 'water': 100}
        with self.assertRaises(ValueError):
            p = Pantry()
        del Pantry.store['Kryptonite']

if __name__ == '__main__':
    unittest.main()