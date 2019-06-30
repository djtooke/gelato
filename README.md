# Gelato recipe calculator

A calculator for formulating perfect gelato recipes! In object-oriented Python.

### Gelato basics

In order to ensure that your gelato will set properly when you freeze it, its constituents should be balanced within certain ranges:

- Fat: 6-12%
- Sugar: 16-22%
- Lean milk solids: 8-12%
- Water: 58-68%
- Dry residual mass: 32-42%

Dry residual total includes fat, sugar, lean milk solids, and any other solids.

As you create your gelato you must balance the quantities of your ingredients to ensure that overall your gelato mix keeps within the above ranges. If you manage it, your gelato should freeze perfectly...!

### Setup and instructions

For now, this is a calculator operated from within the Python REPL.

- Clone this repository
- Open your Python REPL and import the `Gelato`, `Ingredient` and `Pantry` classes from their requisite python files in the `calc` module
- Intantiate some Python objects and have fun playing with them to create your gelato recipe!

#### Pantry and ingredients

The easiest way to create ingredient objects is to get them from the `pantry`. To see a list of available ingredients:

`p = Pantry()`

`p.list_ingredients()`

To get an ingredient object from the pantry, use the `get_ingredient` method, passing in a string of the ingredient name, and the number of grams:

`cream = p.get_ingredient('cream 35%', 220)`

This will return an ingredient object, which contains a series of attributes that detail its percentages of `fat`, `sugar`, `lm_s` (lean milk solids, `oth_s` (other solids), `water` and `dry` mass. These are pre-populated by the pantry on instantiation.

Alternatively, if you want to create an ingredient from scratch and know the percentages of its constituent `fat`, `sugar`, `lm_s`, `oth_s`, and `water` percentages, you can instantiate an `Ingredient` object with these values, followed by its name as a string and the grams:

`honey = Ingredient(0, 80, 0, 0, 20, 'Honey', 100)'

These constituent percentages can be integers or floats (or a combination) but must add up to 100%. `dry` mass is calculated automatically. 
 
#### Gelato objects

You can add ingredients to a gelato object:

`g = Gelato()`

`g.add_ingredient(cream, honey)`

These are now stored within a list as `g.ingredients`. The gelato object will then automatically calculate a series of other values: 

`g.totals`: a dictionary detailing the total number of grams of each constituent (sugar, fat etc.) in the gelato
`g.percs`: a dictionary giving the percentages of each constituent within the gelato
`g.results`: a dictionary indicating whether each constituent is within the acceptable range, or too high or too low.

These can be accessed directly, or if preferred you can pretty print their values in a more readable way using `g.print_ingredients()`, `g.print_totals()`, `g.print_percs()`, `g.print_results()` or for a full overview, `g.print_all()`.

You can remove an ingredient or change the number of grams of an ingredient with built-in methods:

`g.remove_ingredient(honey)`

`g.update_quantity(cream, 300)`

These methods will automatically recalculate the percentages, totals, and results.


#### Coming soon!

The next step will be to transform this calculator into the backend of a web based app, allowing you to create and add ingredients with a GUI.