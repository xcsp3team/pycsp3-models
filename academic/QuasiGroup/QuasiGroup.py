"""
This is the [problem 003](https://www.csplib.org/Problems/prob003/) of the CSPLib:

"*An order m quasigroup is a Latin square of size m. That is, a m×m multiplication table in which each element occurs once in every row and column.:*"

### Example

```
1    2   3   4
4    1   2   3
3    4   1   2
2    3   4   1
```

## Data
A number n, the size of the square.

## Model(s)
There are 7 variants of this problem.

You can find a step-by-step modeling process in this [Jupyter notebook](https://pycsp.org/documentation/models/CSP/Quasigroup/).


constraints: AllDifferentMatrix, Element



## Command Line

python QuasiGroup.py
python QuasiGroup.py -data=8 -variant=base-v3
python QuasiGroup.py -data=5 -variant=base-v4
python QuasiGroup.py -data=8 -variant=base-v5
python QuasiGroup.py -data=8 -variant=base-v6
python QuasiGroup.py -data=9 -variant=base-v7
python QuasiGroup.py -data=8 -variant=aux-v3
python QuasiGroup.py -data=5 -variant=aux-v4
python QuasiGroup.py -data=8 -variant=aux-v5
python QuasiGroup.py -data=9 -variant=aux-v7

## Tags
 academic notebook csplib
 """

from pycsp3 import *

n = data or 8

pairs = [(i, j) for i in range(n) for j in range(n)]

# x[i][j] is the value at row i and column j of the quasi-group
x = VarArray(size=[n, n], dom=range(n))

satisfy(
    # ensuring a Latin square
    AllDifferent(x, matrix=True),

    # ensuring idempotence  tag(idempotence)
    [x[i][i] == i for i in range(n)]
)

if variant("base"):
    if subvariant("v3"):
        satisfy(
            x[x[i][j], x[j][i]] == i for i, j in pairs
        )
    elif subvariant("v4"):
        satisfy(
            x[x[j][i], x[i][j]] == i for i, j in pairs
        )
    elif subvariant("v5"):
        satisfy(
            x[x[x[j][i], j], j] == i for i, j in pairs
        )
    elif subvariant("v6"):
        satisfy(
            x[x[i][j], j] == x[i, x[i][j]] for i, j in pairs
        )
    elif subvariant("v7"):
        satisfy(
            x[x[j][i], j] == x[i, x[j][i]] for i, j in pairs
        )
elif variant("aux"):
    if subvariant("v3"):
        y = VarArray(size=[n, n], dom=range(n * n))

        satisfy(
            [x[y[i][j]] == i for i, j in pairs if i != j],
            [y[i][j] == x[i][j] * n + x[j][i] for i, j in pairs if i != j]
        )
    elif subvariant("v4"):
        y = VarArray(size=[n, n], dom=range(n * n))

        satisfy(
            [x[y[i][j]] == i for i, j in pairs if i != j],
            [y[i][j] == x[j][i] * n + x[i][j] for i, j in pairs if i != j]
        )
    elif subvariant("v5"):
        y = VarArray(size=[n, n], dom=range(n))

        satisfy(
            [x[:, i][x[i][j]] == y[i][j] for i, j in pairs if i != j],
            [x[:, i][y[i][j]] == j for i, j in pairs if i != j]
        )
    elif subvariant("v7"):
        y = VarArray(size=[n, n], dom=range(n))

        satisfy(
            (x[:, j][x[j][i]] == y[i][j], x[i][x[j][i]] == y[i][j]) for i, j in pairs if i != j
        )

""" Comments
1) note that we can post tuples of constraints instead of individually, as demonstrated in aux-v7
"""