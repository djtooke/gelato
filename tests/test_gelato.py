import unittest

from calc.gelato import Gelato
from calc.ingredient import Ingredient
from calc.evaluate import Result

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

    def test_evaluation(self):
        g = Gelato()
        i_1 = Ingredient(9.1, 16.8, 10.5, 0.5, 63.1, 'Gorgonzola & Honey Gelato', 1000)
        g.add_ingredient(i_1)
        self.assertEqual(g.results, {'fat': Result.OKAY,
                                     'sugar': Result.OKAY,
                                     'lm_s': Result.OKAY,
                                     'oth_s': Result.OKAY,
                                     'water': Result.OKAY,
                                     'dry': Result.OKAY})
        g = Gelato()
        i_2 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 1000)
        g.add_ingredient(i_2)
        self.assertEqual(g.results, {'fat': Result.TOO_HIGH,
                                     'sugar': Result.OKAY,
                                     'lm_s': Result.TOO_HIGH,
                                     'oth_s': Result.OKAY,
                                     'water': Result.TOO_LOW,
                                     'dry': Result.TOO_HIGH})

    def test_remove_ingredient(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        i_2 = Ingredient(0, 0, 0, 0, 100, 'Water', 100)
        g.add_ingredient(i_1)
        g.add_ingredient(i_2)
        self.assertEqual(g.totals['fat'], 20)
        self.assertEqual(g.totals['sugar'], 20)
        self.assertEqual(g.totals['lm_s'], 20)
        self.assertEqual(g.totals['oth_s'], 20)
        self.assertEqual(g.totals['water'], 120)
        self.assertEqual(g.totals['dry'], 80)
        self.assertEqual(g.totals['grams'], 200)
        g.remove_ingredient(i_2)
        self.assertEqual(g.percs['fat'], 20)
        self.assertEqual(g.percs['sugar'], 20)
        self.assertEqual(g.percs['lm_s'], 20)
        self.assertEqual(g.percs['oth_s'], 20)
        self.assertEqual(g.percs['water'], 20)
        self.assertEqual(g.percs['dry'], 80)
        self.assertEqual(g.totals['fat'], 20)
        self.assertEqual(g.totals['sugar'], 20)
        self.assertEqual(g.totals['lm_s'], 20)
        self.assertEqual(g.totals['oth_s'], 20)
        self.assertEqual(g.totals['water'], 20)
        self.assertEqual(g.totals['dry'], 80)
        self.assertEqual(g.totals['grams'], 100)

    def test_update_quantity(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        i_2 = Ingredient(0, 0, 0, 0, 100, 'Water', 100)
        g.add_ingredient(i_1, i_2)
        g.update_quantity(i_1, 200)
        self.assertEqual(g.totals['fat'], 40)
        self.assertEqual(g.totals['sugar'], 40)
        self.assertEqual(g.totals['lm_s'], 40)
        self.assertEqual(g.totals['oth_s'], 40)
        self.assertEqual(g.totals['water'], 140)
        self.assertEqual(g.totals['dry'], 160)
        self.assertEqual(g.totals['grams'], 300)

    def test_ingredient_already_added(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        g.add_ingredient(i_1)
        with self.assertRaises(ValueError):
            g.add_ingredient(i_1)

    def test_ingredient_not_yet_added(self):
        g = Gelato()
        i_1 = Ingredient(20, 20, 20, 20, 20, 'Phlogiston', 100)
        i_2 = Ingredient(0, 0, 0, 0, 100, 'Water', 100)
        g.add_ingredient(i_1)
        with self.assertRaises(ValueError):
            g.remove_ingredient(i_2)

    def test_all(self):
        g = Gelato()
        milk = Ingredient(1.6, 0, 9, 0, 89.4, 'Milk', 1000)
        gorgonzola = Ingredient(28, 0.1, 20, 2, 49.9, 'Gorgonzola', 280)
        honey = Ingredient(0, 80, 0, 0, 20, 'Honey', 100)
        sucrose = Ingredient(0, 100, 0, 0, 0, 'Sucrose', 190)
        dextrose = Ingredient(0, 92, 0, 0, 8, 'Dextrose', 50)
        lmp = Ingredient(0, 0, 97, 0, 3, 'LMP', 40)
        stabilisers = Ingredient(0, 0, 0, 100, 0, 'Stabilisers', 4)
        cream = Ingredient(35, 0, 6, 0, 59, 'Cream', 220)

        g.add_ingredient(milk, gorgonzola, honey, sucrose)
        g.add_ingredient(dextrose, lmp)
        g.add_ingredient(stabilisers)
        g.add_ingredient(cream)

        self.assertEqual(g.ingredients, [milk, gorgonzola, honey, sucrose, dextrose, lmp, stabilisers, cream])
        self.assertEqual(g.results, {'fat': Result.OKAY,
                                     'sugar': Result.OKAY,
                                     'lm_s': Result.OKAY,
                                     'oth_s': Result.OKAY,
                                     'water': Result.OKAY,
                                     'dry': Result.OKAY})
        self.assertEqual(g.percs, {'fat': 9.1,
                                     'sugar': 16.8,
                                     'lm_s': 10.5,
                                     'oth_s': 0.5,
                                     'water': 63.1,
                                     'dry': 36.9})

        self.assertEqual(g.totals, {'fat': 171.4,
                                     'sugar': 316.3,
                                     'lm_s': 198.0,
                                     'oth_s': 9.6,
                                     'water': 1188.7,
                                     'dry': 695.3,
                                     'grams': 1884})

if __name__ == '__main__':
    unittest.main()