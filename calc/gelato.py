from calc.ingredient import Ingredient, CONSTITUENTS
from calc.evaluate import AIM, Result
import copy


class Gelato:

    def __init__(self):
        self.ingredients = []
        self.totals = {}
        self.percs = {}
        self.results = {}
        self._reset_counters()

    def add_ingredient(self, *args):
        [self._verify_ingredient(ing) for ing in args]
        [self._verify_ingredient_not_added(ing) for ing in args]
        self.ingredients.extend(args)
        self._recalculate_all()

    def remove_ingredient(self, ing):
        self._verify_ingredient_added(ing)
        self.ingredients.remove(ing)
        self._recalculate_all()

    def update_quantity(self, ing, grams):
        self._verify_ingredient_added(ing)
        ing.update_quantity(grams)
        self._recalculate_all()

    def _recalculate_all(self):
        self._reset_counters()
        self._amend_totals()
        self._amend_percentages()
        self._evaluate_results()

    def _reset_counters(self):
        self.percs = {c: 0 for c in CONSTITUENTS}
        self.totals = copy.copy(self.percs)
        self.totals['grams'] = 0
        self.results = copy.copy(self.percs)

    def _amend_totals(self):
        for ing in self.ingredients:
            self.totals['fat'] += ing.fat / 100 * ing.grams
            self.totals['sugar'] += ing.sugar / 100 * ing.grams
            self.totals['lm_s'] += ing.lm_s / 100 * ing.grams
            self.totals['oth_s'] += ing.oth_s / 100 * ing.grams
            self.totals['water'] += ing.water / 100 * ing.grams
            self.totals['grams'] += ing.grams
        self.totals['dry'] = self.totals['grams'] - self.totals['water']
        self._round_numbers(self.totals)

    def _amend_percentages(self):
        self.percs = {k: v / self.totals['grams'] * 100 for k, v in self.totals.items()}
        del self.percs['grams']
        self._round_numbers(self.percs)

    def _evaluate_results(self):
        for k, v in self.percs.items():
            if v < AIM[k][0]:
                self.results[k] = Result(0)
            elif v > AIM[k][-1]:
                self.results[k] = Result(2)
            else:
                self.results[k] = Result(1)

    def _round_numbers(self, _dict):
        for k, v in _dict.items():
            _dict[k] = round(v, 1)

    def _verify_ingredient(self, ing):
        if type(ing) != Ingredient:
            raise TypeError('Attempted to add an ingredient that was not of type Ingredient: {}'.format(ing))

    def _verify_ingredient_added(self, ing):
        if ing not in self.ingredients:
            raise ValueError('{} not in list of ingredients'.format(ing))

    def _verify_ingredient_not_added(self, ing):
        if ing in self.ingredients:
            raise ValueError('{} already in list of ingredients'.format(ing))

