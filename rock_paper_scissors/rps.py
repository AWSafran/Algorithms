#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  first_turn = [["rock"], ["paper"], ["scissors"]]
  return_arr = []
  if n == 0:
    return [[]]
  elif n == 1:
    return first_turn
  else:
    for turn in first_turn:
      for existing in rock_paper_scissors(n - 1):
        return_arr.append(turn + existing)
  return return_arr


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')