#!/usr/bin/python

import sys

def making_change(amount, denominations):

  print(f"Running function for {amount}")

  cache_one = [1] * (amount + 1)
  cache_two = [0] * (amount + 1)
  cache_three = [0] * (amount + 1)
  cache_four = [0] * (amount + 1)
  cache_five = [0] * (amount + 1)

  
  def making_change_recursive(amount, denominations):
    nonlocal cache_one
    nonlocal cache_two
    nonlocal cache_three
    nonlocal cache_four
    nonlocal cache_five

    if len(denominations) == 1:
      cache = cache_one
    elif len(denominations) == 2:
      cache = cache_two
    elif len(denominations) == 3:
      cache = cache_three
    elif len(denominations) == 4:
      cache = cache_four
    elif len(denominations) == 5:
      cache = cache_five

    if cache[amount] != 0:
      return cache[amount]
    
    if amount < 5:
      cache[amount] = 1
      #return 1
    else:

      running_total = 0
      for i in range(len(denominations)):
        coin = denominations[i]

        if amount >= coin:
          new_denoms = []

          for num in denominations:
            if num <= coin: # Force it to pick coins in descending order of size, since this is combination, not permutation
              new_denoms.append(num) # Sadly, this breaks the memoization that I had tried to set up
          running_total += making_change_recursive(amount - coin, new_denoms)
          cache[amount] = running_total


    return cache[amount]
    #return running_total

  # If amount is huuuuge, try pre-populating the cache by running smaller amount that we know will work
  if amount > 2000:
    making_change_recursive(2000, denominations)

  if amount > 5000:
    making_change_recursive(5000, denominations)
    making_change_recursive(6000, denominations)
    making_change_recursive(7000, denominations)
    making_change_recursive(8000, denominations)

  return making_change_recursive(amount, denominations)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")