#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  item_number = 0
  max_batches = 0
  for item in recipe:
    if not item in ingredients or ingredients[item] < recipe[item]:
      return 0
    else:
      if max_batches > (ingredients[item] // recipe[item]) or item_number == 0:
        max_batches = ingredients[item] // recipe[item]
        item_number += 1

  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))