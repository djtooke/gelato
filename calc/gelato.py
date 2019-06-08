from calc.ingredient import Ingredient
from calc.evaluate import AIM, Result
import copy

CONSTITUENTS = ['fat', 'sugar', 'lm_s', 'oth_s', 'water', 'dry']

class Gelato:

    def __init__(self):
        self.ingredients = []
        self.totals = {}
        self.percs = {}
        self.results = {}
        self._reset_counters()

    def add_ingredient(self, *args):
        [self._verify_ingredient(ing) for ing in args]
        self.ingredients.extend(args)
        self._reset_counters()
        self.amend_totals()
        self.amend_percentages()
        self._evaluate()

    def amend_totals(self):
        for ing in self.ingredients:
            self.totals['fat'] += ing.fat / 100 * ing.grams
            self.totals['sugar'] += ing.sugar / 100 * ing.grams
            self.totals['lm_s'] += ing.lm_s / 100 * ing.grams
            self.totals['oth_s'] += ing.oth_s / 100 * ing.grams
            self.totals['water'] += ing.water / 100 * ing.grams
            self.totals['grams'] += ing.grams
        self.totals['dry'] = self.totals['grams'] - self.totals['water']

    def amend_percentages(self):
        self.percs = {k: round(v / self.totals['grams'] * 100, 1) for k, v in self.totals.items()}
        del self.percs['grams']

    def _verify_ingredient(self, ing):
        if type(ing) != Ingredient:
            raise TypeError('Attempted to add an ingredient that was not of type Ingredient: {}'.format(ing))

    def _evaluate(self):
        for k, v in self.percs.items():
            if v < AIM[k][0]:
                self.results[k] = Result(0)
            elif v > AIM[k][-1]:
                self.results[k] = Result(2)
            else:
                self.results[k] = Result(1)

    def _reset_counters(self):
        self.percs = {c: 0 for c in CONSTITUENTS}
        self.totals = copy.copy(self.percs)
        self.totals['grams'] = 0
        self.results = copy.copy(self.percs)
