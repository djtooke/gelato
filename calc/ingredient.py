class Ingredient:

    def __init__(self, fat: int, sugar: int, lm_s: int, oth_s: int, water: int):
        '''
        Initialise ingredient object, saving constituent percentages
        :param fat:
        :param sugar:
        :param lm_s:
        :param oth_s:
        :param water:
        '''

        self._verify_constituents(fat, sugar, lm_s, oth_s, water)

        self.fat = fat
        self.sugar = sugar
        self.lm_s = lm_s
        self.oth_s = oth_s
        self.water = water
        self.dry = 100 - water


    def _verify_constituents(self, fat, sugar, lm_s, oth_s, water):
        '''
        Verify that constituents are numbers and add up to 100%
        :param fat:
        :param sugar:
        :param lm_s:
        :param oth_s:
        :param water:
        :return:
        '''

        # Check all arguments are either integers or floats
        if not all(isinstance(x, (int, float)) for x in [fat, sugar, lm_s, oth_s, water]):
            raise TypeError('Constituent percentages must be integers or floats')

        # Check sum of constituent percentages is 100%
        perc = sum([fat, sugar, lm_s, oth_s, water])
        if perc != 100:
            raise ValueError('Constituent values add up to {}% rather than 100%'.format(perc))