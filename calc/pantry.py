from calc.ingredient import Ingredient

class Pantry:

    store = {
        # Water and milk products
        'water': {'fat': 0, 'sugar': 0, 'lm_s': 0, 'oth_s': 0, 'water': 100},
        'whole milk': {'fat': 3.5, 'sugar': 0, 'lm_s': 9, 'oth_s': 0, 'water': 87.5},
        'skimmed milk': {'fat': 1.6, 'sugar': 0, 'lm_s': 9, 'oth_s': 0, 'water': 89.4},
        'whole milk powder': {'fat': 26, 'sugar': 0, 'lm_s': 72, 'oth_s': 0, 'water': 2},
        'skimmed milk powder': {'fat': 0, 'sugar': 0, 'lm_s': 97, 'oth_s': 0, 'water': 3},
        'evaporated whole milk': {'fat': 8, 'sugar': 0, 'lm_s': 18, 'oth_s': 0, 'water': 74},
        'condensed whole milk': {'fat': 9, 'sugar': 43, 'lm_s': 22, 'oth_s': 0, 'water': 26},
        'condensed skimmed milk': {'fat': 0, 'sugar': 52, 'lm_s': 27, 'oth_s': 0, 'water': 21},
        'cream 30%': {'fat': 30, 'sugar': 0, 'lm_s': 6, 'oth_s': 0, 'water': 64},
        'cream 35%': {'fat': 35, 'sugar': 0, 'lm_s': 6, 'oth_s': 0, 'water': 59},
        'cream 40%': {'fat': 40, 'sugar': 0, 'lm_s': 5, 'oth_s': 0, 'water': 55},
        'butter': {'fat': 84, 'sugar': 0, 'lm_s': 0, 'oth_s': 0, 'water': 16},
        'dehydrated butter': {'fat': 99, 'sugar': 0, 'lm_s': 0, 'oth_s': 0, 'water': 1},
        'mascarpone': {'fat': 44, 'sugar': 2, 'lm_s': 6, 'oth_s': 0, 'water': 48},
        'gorgonzola': {'fat': 28, 'sugar': 0.1, 'lm_s': 20, 'oth_s': 2, 'water': 49.9},

        # Sugar and sweeteners
        'sucrose': {'fat': 0, 'sugar': 100, 'lm_s': 0, 'oth_s': 0, 'water': 0},
        'fructose': {'fat': 0, 'sugar': 100, 'lm_s': 0, 'oth_s': 0, 'water': 0},
        'dextrose': {'fat': 0, 'sugar': 92, 'lm_s': 0, 'oth_s': 0, 'water': 8},
        'inverted sugar': {'fat': 0, 'sugar': 70, 'lm_s': 0, 'oth_s': 0, 'water': 30},
        'glucose': {'fat': 0, 'sugar': 80, 'lm_s': 0, 'oth_s': 0, 'water': 20},
        'honey': {'fat': 0, 'sugar': 80, 'lm_s': 0, 'oth_s': 0, 'water': 20},

        # Raw materials
        'whole egg': {'fat': 10, 'sugar': 0, 'lm_s': 0, 'oth_s': 15, 'water': 75},
        'egg yolk': {'fat': 32, 'sugar': 0, 'lm_s': 0, 'oth_s': 18, 'water': 50},
        'dried egg yolk': {'fat': 66, 'sugar': 0, 'lm_s': 0, 'oth_s': 32, 'water': 2},
        'egg white': {'fat': 0, 'sugar': 0, 'lm_s': 0, 'oth_s': 15, 'water': 85},
        'cocoa powder (10-12% cocoa butter)': {'fat': 11, 'sugar': 0, 'lm_s': 0, 'oth_s': 84, 'water': 5},
        'cocoa powder (22-24% cocoa butter)': {'fat': 23, 'sugar': 0, 'lm_s': 0, 'oth_s': 72, 'water': 5},
        'hazelnut paste': {'fat': 60, 'sugar': 0, 'lm_s': 0, 'oth_s': 35, 'water': 5},
        'torrone paste': {'fat': 15, 'sugar': 40, 'lm_s': 0, 'oth_s': 45, 'water': 0},
        'almond paste': {'fat': 55, 'sugar': 0, 'lm_s': 0, 'oth_s': 45, 'water': 0},
        'pistachio paste': {'fat': 55, 'sugar': 0, 'lm_s': 0, 'oth_s': 45, 'water': 0},
        'walnut paste': {'fat': 60, 'sugar': 0, 'lm_s': 0, 'oth_s': 40, 'water': 0},
        'toasted coffee powder': {'fat': 14, 'sugar': 0, 'lm_s': 0, 'oth_s': 86, 'water': 0},
        'coconut oil (dehydrated)': {'fat': 100, 'sugar': 0, 'lm_s': 0, 'oth_s': 0, 'water': 0},
        'stabilisers (pure)': {'fat': 0, 'sugar': 0, 'lm_s': 0, 'oth_s': 100, 'water': 0},

        # Fruit
        'banana': {'fat': 0, 'sugar': 18, 'lm_s': 0, 'oth_s': 7, 'water': 75},
        'figs': {'fat': 0, 'sugar': 15, 'lm_s': 0, 'oth_s': 5, 'water': 80},
        'cherries': {'fat': 0, 'sugar': 12, 'lm_s': 0, 'oth_s': 8, 'water': 80},
        'grapes': {'fat': 0, 'sugar': 20, 'lm_s': 0, 'oth_s': 5, 'water': 75},
        'other juicy fruit' : {'fat': 0, 'sugar': 10, 'lm_s': 0, 'oth_s': 5, 'water': 85},

        # Fruit conserves
        'pineapple in syrup': {'fat': 0, 'sugar': 22, 'lm_s': 0, 'oth_s': 3, 'water': 75},
        'pineapple juice': {'fat': 0, 'sugar': 10, 'lm_s': 0, 'oth_s': 3, 'water': 87}
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

    def list_ingredients(self):
        print('List of available ingredients:')
        for k in self.store.keys():
            print(k)

