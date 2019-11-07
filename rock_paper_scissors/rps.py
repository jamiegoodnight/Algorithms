#!/usr/bin/python

import sys

all_plays = ['rock', 'paper', 'scissors']
all_combinations = []
new_ar = []


def recursion(ar, num):
    if num == 0:
        all_combinations.append(ar)
        return
    for i in all_plays:
        print("Here is", i)
        recursion(ar+[i], num-1)


def rock_paper_scissors(n):
    if n <= 0:
        return [[]]
    recursion(new_ar, n)
    return all_combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
