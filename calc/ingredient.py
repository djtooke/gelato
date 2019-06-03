class Ingredient:

    def __init__(self, fat: int, sugar: int, lm_s: int, oth_s: int, water: int):

        # Check all arguments are either integers or floats
        if not all(isinstance(x, (int, float)) for x in [fat, sugar, lm_s, oth_s, water]):
            raise TypeError('Constituent percentages must be integers or floats')

        self.fat = fat
        self.sugar = sugar
        self.lm_s = lm_s
        self.oth_s = oth_s
        self.water = water

