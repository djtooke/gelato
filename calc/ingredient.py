class Ingredient:

    def __init__(self, fat, sugar, lm_s, oth_s, water, name: str, grams=0):
        '''
        Initialise ingredient object, saving constituent percentages
        :param fat:
        :param sugar:
        :param lm_s:
        :param oth_s:
        :param water:
        :param name:
        :param grams:
        '''

        self._verify_constituents(fat, sugar, lm_s, oth_s, water, grams)

        self.fat = fat
        self.sugar = sugar
        self.lm_s = lm_s
        self.oth_s = oth_s
        self.water = water
        self.dry = 100 - water
        self.name = name
        self.grams = grams


    def _verify_constituents(self, fat, sugar, lm_s, oth_s, water, grams):
        '''
        Verify that constituents are numbers and add up to 100%
        :param fat:
        :param sugar:
        :param lm_s:
        :param oth_s:
        :param water:
        :param grams:
        :return:
        '''

        # Check all arguments are either integers or floats
        if not all(isinstance(x, (int, float)) for x in [fat, sugar, lm_s, oth_s, water, grams]):
            raise TypeError('Constituent percentages and grams must be integers or floats')

        # Check sum of constituent percentages is 100%
        total = sum([fat, sugar, lm_s, oth_s, water])
        if total != 100:
            raise ValueError('Constituent values add up to {}% rather than 100%'.format(total))
