#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if cache == None:
    cache = [0 for i in range(n + 1)]

  def eating_cookies_recursive(n):
    nonlocal cache
    if cache[n] != 0:
      return cache[n]
    if n <= 1:
      cache[n] = 1
    elif n == 2:
      cache[n] = 2
    else:
      cache[n] = eating_cookies_recursive(n - 1) + eating_cookies_recursive(n - 2) + eating_cookies_recursive(n - 3)

    return cache[n]

  return eating_cookies_recursive(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')