import unittest

from calc.ingredient import Ingredient

class TestIngredients(unittest.TestCase):

    def test_class_exists(self):
        self.assertTrue( Ingredient(20, 20, 20, 20, 20) )

    def test_ingredient_constituents(self):
        ing = Ingredient(20, 20, 20, 20, 20)
        self.assertEqual(ing.fat, 20)
        self.assertEqual(ing.sugar, 20)
        self.assertEqual(ing.lm_s, 20)
        self.assertEqual(ing.oth_s, 20)
        self.assertEqual(ing.water, 20)

    def test_raise_on_invalid_percentage(self):
        with self.assertRaises(TypeError):
            Ingredient('20', 20, 20, 20, 20)
        with self.assertRaises(TypeError):
            Ingredient(20, '20', 20, 20, 20)
        with self.assertRaises(TypeError):
            Ingredient(20, 20, '20', 20, 20)
        with self.assertRaises(TypeError):
            Ingredient(20, 20, 20, '20', 20)
        with self.assertRaises(TypeError):
            Ingredient(20, 20, 20, 20, '20')

if __name__ == '__main__':
    unittest.main()