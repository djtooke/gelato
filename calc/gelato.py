from calc.ingredient import Ingredient

class Gelato:

    def __init__(self):
        self.ingredients = []


    def add_ingredient(self, *args):
        [self._verify_ingredient(ing) for ing in args]
        self.ingredients.extend(args)

    def _verify_ingredient(self, ing):
        if type(ing) != Ingredient:
            raise TypeError('Attempted to add an ingredient that was not of type Ingredient: {}'.format(ing))