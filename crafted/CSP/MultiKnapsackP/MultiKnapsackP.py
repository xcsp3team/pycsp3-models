"""
Multi Dimensional Knapsack Problem.

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2014 Minizinc challenge.
No Licence was explicitly mentioned (MIT Licence assumed).

## Data Example
  1-06.json

## Model
  constraints: Sum

## Execution
  python MultiKnapsackP.py -data=<datafile.json>
  python MultiKnapsackP.py -data=<datafile.dzn> -parser=MultiKnapsack_ParserZ.py

## Links
  - https://www.minizinc.org/challenge2014/results2014.html

## Tags
  crafted, mzn14
"""

from pycsp3 import *

weights, profits, sizes, z = data
nItems, nBins = len(profits), len(sizes)

# x[i] is 1 if the ith item is selected
x = VarArray(size=nItems, dom={0, 1})

satisfy(
    # not exceeding the capacity of each bin
    [x * weights[j] <= sizes[j] for j in range(nBins)],

    # ensuring we get the fixed objective value
    profits * x == z
)