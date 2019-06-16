from calc.ingredient import Ingredient

class Pantry:

    store = {
        # Water and milk products
        'water': {'sugar': 0, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 100},
        'whole milk': {'sugar': 0, 'fat': 3.5, 'lm_s': 9, 'oth_s': 0, 'water': 87.5},
        'skimmed milk': {'sugar': 0, 'fat': 1.6, 'lm_s': 9, 'oth_s': 0, 'water': 89.4},
        'whole milk powder': {'sugar': 0, 'fat': 26, 'lm_s': 72, 'oth_s': 0, 'water': 2},
        'skimmed milk powder': {'sugar': 0, 'fat': 0, 'lm_s': 97, 'oth_s': 0, 'water': 3},
        'evaporated whole milk': {'sugar': 0, 'fat': 8, 'lm_s': 18, 'oth_s': 0, 'water': 74},
        'condensed whole milk': {'sugar': 43, 'fat': 9, 'lm_s': 22, 'oth_s': 0, 'water': 26},
        'condensed skimmed milk': {'sugar': 52, 'fat': 0, 'lm_s': 27, 'oth_s': 0, 'water': 21},
        'cream 30%': {'sugar': 0, 'fat': 30, 'lm_s': 6, 'oth_s': 0, 'water': 64},
        'cream 35%': {'sugar': 0, 'fat': 35, 'lm_s': 6, 'oth_s': 0, 'water': 59},
        'cream 40%': {'sugar': 0, 'fat': 40, 'lm_s': 5, 'oth_s': 0, 'water': 55},
        'butter': {'sugar': 0, 'fat': 84, 'lm_s': 0, 'oth_s': 0, 'water': 16},
        'dehydrated butter': {'sugar': 0, 'fat': 99, 'lm_s': 0, 'oth_s': 0, 'water': 1},
        'mascarpone': {'sugar': 2, 'fat': 44, 'lm_s': 6, 'oth_s': 0, 'water': 48},

        # Sugar and sweeteners
        'sucrose': {'sugar': 100, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 0},
        'fructose': {'sugar': 100, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 0},
        'dextrose': {'sugar': 92, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 8},
        'inverted sugar': {'sugar': 70, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 30},
        'glucose': {'sugar': 80, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 20},
        'honey': {'sugar': 80, 'fat': 0, 'lm_s': 0, 'oth_s': 0, 'water': 20},

        # Raw materials
        'whole egg': {'sugar': 0, 'fat': 10, 'lm_s': 0, 'oth_s': 15, 'water': 75},
        'egg yolk': {'sugar': 0, 'fat': 32, 'lm_s': 0, 'oth_s': 18, 'water': 50},
        'dried egg yolk': {'sugar': 0, 'fat': 66, 'lm_s': 0, 'oth_s': 32, 'water': 2},
        'egg white': {'sugar': 0, 'fat': 0, 'lm_s': 0, 'oth_s': 15, 'water': 85},
        'cocoa powder (10-12% cocoa butter)': {'sugar': 0, 'fat': 11, 'lm_s': 0, 'oth_s': 84, 'water': 5},
        'cocoa powder (22-24% cocoa butter)': {'sugar': 0, 'fat': 23, 'lm_s': 0, 'oth_s': 72, 'water': 5},
        'hazelnut paste': {'sugar': 0, 'fat': 60, 'lm_s': 0, 'oth_s': 35, 'water': 5},
        'torrone paste': {'sugar': 40, 'fat': 15, 'lm_s': 0, 'oth_s': 45, 'water': 0},
        'almond paste': {'sugar': 0, 'fat': 55, 'lm_s': 0, 'oth_s': 45, 'water': 0},
        'pistachio paste': {'sugar': 0, 'fat': 55, 'lm_s': 0, 'oth_s': 45, 'water': 0},
        'walnut paste': {'sugar': 0, 'fat': 60, 'lm_s': 0, 'oth_s': 40, 'water': 0},
        'toasted coffee powder': {'sugar': 0, 'fat': 14, 'lm_s': 0, 'oth_s': 86, 'water': 0},
        'coconut oil (dehydrated)': {'sugar': 0, 'fat': 100, 'lm_s': 0, 'oth_s': 0, 'water': 0},
        'stabilisers (pure)': {'sugar': 0, 'fat': 0, 'lm_s': 0, 'oth_s': 100, 'water': 0},

        # Fruit
        'banana': {'sugar': 18, 'fat': 0, 'lm_s': 0, 'oth_s': 7, 'water': 75},
        'figs': {'sugar': 15, 'fat': 0, 'lm_s': 0, 'oth_s': 5, 'water': 80},
        'cherries': {'sugar': 12, 'fat': 0, 'lm_s': 0, 'oth_s': 8, 'water': 80},
        'grapes': {'sugar': 20, 'fat': 0, 'lm_s': 0, 'oth_s': 5, 'water': 75},
        'other juicy fruit' : {'sugar': 10, 'fat': 0, 'lm_s': 0, 'oth_s': 5, 'water': 85},

        # Fruit conserves
        'pineapple in syrup': {'sugar': 22, 'fat': 0, 'lm_s': 0, 'oth_s': 3, 'water': 75},
        'pineapple juice': {'sugar': 10, 'fat': 0, 'lm_s': 0, 'oth_s': 3, 'water': 87}
    }


    def __init__(self):

        # Check the value of each ingredient to ensure no new erroneous entries
        for name, consts in Pantry.store.items():
            if sum(consts.values()) != 100:
                raise ValueError('Values do not add up to 100% for {} ingredient'.format(name))

    def get_ingredient(self, name, grams):
        ing = Pantry.store.get(name)
        if not ing:
            raise ValueError('Ingredient {} does not exist in the pantry'.format(name))
        return Ingredient(name=name, grams=grams, **ing)


