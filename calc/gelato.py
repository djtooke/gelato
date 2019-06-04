from calc.ingredient import Ingredient

class Gelato:

    def __init__(self):
        self.ingredients = []
        self.totals = {
            'fat': 0,
            'sugar': 0,
            'lm_s': 0,
            'oth_s': 0,
            'water': 0,
            'dry': 0,
            'grams': 0
        }

    def add_ingredient(self, *args):
        [self._verify_ingredient(ing) for ing in args]
        self.ingredients.extend(args)
        self.amend_totals()

    def amend_totals(self):
        self.totals = {k: 0 for k, v in self.totals.items()}
        for ing in self.ingredients:
            self.totals['fat'] += ing.fat / 100 * ing.grams
            self.totals['sugar'] += ing.sugar / 100 * ing.grams
            self.totals['lm_s'] += ing.lm_s / 100 * ing.grams
            self.totals['oth_s'] += ing.oth_s / 100 * ing.grams
            self.totals['water'] += ing.water / 100 * ing.grams
            self.totals['grams'] += ing.grams
        self.totals['dry'] = self.totals['grams'] - self.totals['water']

    def _verify_ingredient(self, ing):
        if type(ing) != Ingredient:
            raise TypeError('Attempted to add an ingredient that was not of type Ingredient: {}'.format(ing))
