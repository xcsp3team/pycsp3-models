"""
This is the [problem 006](https://www.csplib.org/Problems/prob006/) of the CSPLib:


A Golomb ruler is defined as a set of $n$ integers $0 = a_1 < a_2 < ... < a_n$ such that the $n \times (n-1)/2$ differences $a_j - a_i$, $1 \leq i < j \leq n$, are distinct.
Such a ruler is said to contain $n$ marks (or ticks) and to be of length $a_n$.
The objective is to find optimal rulers (i.e., rulers of minimum length).

An optimal Golomb ruler with 4 ticks. <small>Image from [commons.wikimedia.org](https://commons.wikimedia.org/wiki/File:Golomb_Ruler-4.svg) </small>
<img src="https://pycsp.org/assets/notebooks/figures/golomb.png" alt="Golomb ruler" width="300" />

This problem (and its variants) is said to have many practical applications including sensor placements for x-ray crystallography and radio astronomy.


### Example

The optimum for n=8

```
    0  1  4  9  15  22  32  34
```


## Data
A number n, the number of integers.

## Model(s)
You can find a step-by-step modeling process in this [Jupyter notebook](https://pycsp.org/documentation/models/CSP/GolombRuler/).

There are 3 variants:
 - one with all different constraint based on expression
 - one with auxilliary variables
 - and one with  intension constraints.

 constraints: Intension, AllDifferent


## Command Line


python GolombRuler.py
python GolombRuler.py -data=10
python GolombRuler.py -data=10 -variant=dec
python GolombRuler.py -data=10 -variant=aux

## Tags
 academic

"""

from pycsp3 import *

n = data or 8
ub = n * n + 1  # a trivial upper-bound of an optimal ruler length

# x[i] is the position of the ith tick
x = VarArray(size=n, dom=range(ub))

if not variant():
    satisfy(
        # all distances are different
        AllDifferent(abs(x[i] - x[j]) for i, j in combinations(n, 2))
    )
elif variant("dec"):
    satisfy(
        # all distances are different
        abs(x[i] - x[j]) != abs(x[k] - x[l]) for i, j in combinations(range(n), 2) for k, l in combinations(range(i + 1, n), 2)
    )
elif variant("aux"):
    # y[i][j] is the distance between x[i] and x[j], for i strictly less than j
    y = VarArray(size=[n, n], dom=lambda i, j: range(1, ub) if i < j else None)

    satisfy(
        # all distances are different
        AllDifferent(y),

        # linking variables from both arrays
        [x[j] == x[i] + y[i][j] for i, j in combinations(n, 2)]
    )
    annotate(decision=x)

satisfy(
    # tag(symmetry-breaking)
    [x[0] == 0, Increasing(x, strict=True)]
)

minimize(
    # minimizing the position of the rightmost tick
    Maximum(x)
)


""" Comments
1) one can minimize(x[-1]) provided that symmetry-breaking constraints are not discarded
"""