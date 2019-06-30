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
            raise TypeError('Object is not of type Ingredient: {}'.format(ing))

    def _verify_ingredient_added(self, ing):
        if ing not in self.ingredients:
            raise ValueError('{} not in list of ingredients'.format(ing))

    def _verify_ingredient_not_added(self, ing):
        if ing in self.ingredients:
            raise ValueError('{} already in list of ingredients'.format(ing))

    def print_all(self):
        if not self.ingredients:
            self._warn_empty_ingredients()
            return None
        self.print_ingredients()
        self._print_spacer()
        self.print_totals()
        self._print_spacer()
        self.print_percs()
        self._print_spacer()
        self.print_results()

    def print_ingredients(self):
        if self.ingredients:
            for i in self.ingredients:
                print('{}: {}g'.format(i.name, i.grams))
        else:
            self._warn_empty_ingredients()

    def print_totals(self):
        if self.ingredients:
            print('Totals of constituents in grams:')
            print('    Sugar: {}'.format(self.totals['sugar']))
            print('    Fat: {}'.format(self.totals['fat']))
            print('    Lean milk solids: {}'.format(self.totals['lm_s']))
            print('    Other solids: {}'.format(self.totals['oth_s']))
            print('    Water: {}'.format(self.totals['water']))
            print('    Dry residual mass: {}'.format(self.totals['dry']))
            print('')
            print('Total grams: {}'.format(self.totals['grams']))
        else:
            self._warn_empty_ingredients()

    def print_percs(self):
        if self.ingredients:
            print('Percentages of constituents:')
            print('    Sugar: {}%'.format(self.percs['sugar']))
            print('    Fat: {}%'.format(self.percs['fat']))
            print('    Lean milk solids: {}%'.format(self.percs['lm_s']))
            print('    Other solids: {}%'.format(self.percs['oth_s']))
            print('    Water: {}%'.format(self.percs['water']))
            print('    Dry residual mass: {}%'.format(self.percs['dry']))
        else:
            self._warn_empty_ingredients()

    def print_results(self):
        if self.ingredients:
            print('Evaluation of constituent percentages:')
            print('    Sugar: {}'.format(self.results['sugar'].name))
            print('    Fat: {}'.format(self.results['fat'].name))
            print('    Lean milk solids: {}'.format(self.results['lm_s'].name))
            print('    Other solids: {}'.format(self.results['oth_s'].name))
            print('    Water: {}'.format(self.results['water'].name))
            print('    Dry residual mass: {}'.format(self.results['dry'].name))
        else:
            self._warn_empty_ingredients()

    def _print_spacer(self):
        print('')
        print('==========')
        print('')

    def _warn_empty_ingredients(self):
        print("No ingredients added. Your gelato doesn't exist yet")
        
