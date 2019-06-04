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

    def test_raise_on_adding_non_ingredient(self):
        g = Gelato()
        with self.assertRaises(TypeError):
            g.add_ingredient(None)

    def test_total_calculation(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        i_2 = Ingredient(0, 0, 0, 0, 100, 'Water', 100)
        g.add_ingredient(i_1, i_2)
        self.assertEqual(g.totals['fat'], 20)
        self.assertEqual(g.totals['sugar'], 20)
        self.assertEqual(g.totals['lm_s'], 20)
        self.assertEqual(g.totals['oth_s'], 20)
        self.assertEqual(g.totals['water'], 120)
        self.assertEqual(g.totals['dry'], 80)
        self.assertEqual(g.totals['grams'], 200)
        i_3 = Ingredient(0, 100, 0, 0, 0, 'sugar', 100)
        g.add_ingredient(i_3)
        self.assertEqual(g.totals['fat'], 20)
        self.assertEqual(g.totals['sugar'], 120)
        self.assertEqual(g.totals['lm_s'], 20)
        self.assertEqual(g.totals['oth_s'], 20)
        self.assertEqual(g.totals['water'], 120)
        self.assertEqual(g.totals['dry'], 180)
        self.assertEqual(g.totals['grams'], 300)

    def test_percs_calculation(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        i_2 = Ingredient(0, 0, 0, 0, 100, 'Water', 100)
        g.add_ingredient(i_1)
        self.assertEqual(g.percs['fat'], 20)
        self.assertEqual(g.percs['sugar'], 20)
        self.assertEqual(g.percs['lm_s'], 20)
        self.assertEqual(g.percs['oth_s'], 20)
        self.assertEqual(g.percs['water'], 20)
        self.assertEqual(g.percs['dry'], 80)
        g.add_ingredient(i_2)
        self.assertEqual(g.percs['fat'], 10)
        self.assertEqual(g.percs['sugar'], 10)
        self.assertEqual(g.percs['lm_s'], 10)
        self.assertEqual(g.percs['oth_s'], 10)
        self.assertEqual(g.percs['water'], 60)
        self.assertEqual(g.percs['dry'], 40)
        with self.assertRaises(KeyError):
            g.percs['grams']

if __name__ == '__main__':
    unittest.main()