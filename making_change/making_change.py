#!/usr/bin/python

import sys

def making_change(amount, denominations):

  print(f"Running function for {amount}")

  cache = [0] * (amount + 1)

  def making_change_recursive(amount, denominations):
    nonlocal cache
    
    if amount < 5:
      return 1
    else:

      running_total = 0
      for i in range(len(denominations)):
        coin = denominations[i]

        if amount >= coin:
          new_denoms = []

          for num in denominations:
            if num <= coin:
              new_denoms.append(num)
          running_total += making_change_recursive(amount - coin, new_denoms)


    return running_total

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