#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = 0
    if len(recipe) != len(ingredients):
        return batches

    for key in recipe:
        if batches > 0 and ingredients[key]/recipe[key] > batches:
            break

        if recipe[key] <= ingredients[key]:
            batches = ingredients[key]/recipe[key]

        if recipe[key] > ingredients[key]:
            print("We're in 2", key)
            batches = 0

    return round(batches)


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
