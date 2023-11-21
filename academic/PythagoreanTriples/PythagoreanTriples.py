"""
The Boolean Pythagorean triples problem is a problem from Ramsey theory about whether the positive integers can be colored red and blue
so that no Pythagorean triples consist of all red or all blue members.
The Boolean Pythagorean triples problem was solved by Marijn Heule, Oliver Kullmann and Victor W. Marek in May 2016 through a computer-assisted proof.
More specifically, the problem asks if it is possible to color each of the positive integers either red or blue, so that no triple of integers a, b, c,
satisfying a2 + b2 = c2 are all the same color.
For example, in the Pythagorean triple 3, 4 and 5 (32 + 42 = 52 ), if 3 and 4 are colored red, then 5 must be colored blue.

## Data
  a unique integer n

## Model
  constraints: NValues

## Execution
  - python PythagoreanTriples.py -data=[number]

## Links
  - https://en.wikipedia.org/wiki/Boolean_Pythagorean_triples_problem
  - https://www.cril.univ-artois.fr/XCSP23/competitions/csp/csp

## Tags
  academic, recreational, xcsp23
"""

from pycsp3 import *
from math import sqrt

n = data


def conflicts():
    t = []
    for i in range(1, n + 1):
        i2 = i * i
        for j in range(i + 1, n + 1):
            j2 = j * j
            s = i2 + j2
            if s > n * n:
                break
            sr = int(sqrt(s))
            if sr * sr == s:
                t.append((i, j, sr))
    return t


conflicts = conflicts()

# x[i] is 0 (resp., 1) if integer i is in part/subset 0 (resp., 1)
x = VarArray(size=n + 1, dom={0, 1})

satisfy(
    # setting an arbitrary value to integer 0
    x[0] == 0,

    # ensuring that no Pythagorean triple is present in the same part
    [NValues(x[i], x[j], x[k]) > 1 if not variant() else (x[i], x[j], x[k]) in [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0)]
     for i, j, k in conflicts]
)