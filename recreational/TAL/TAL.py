"""
## Data Example
  frobserved-7-15-11-13-9-1-11-7-4_1.json

## Model
  constraints: Count, Sum, Table

## Execution
  python TAL.py -data=<datafile.json>

## Tags
  realistic
"""
from pycsp3 import *
import math

maxArity, maxHeight, sentence, grammar, tokens, costs = data
nWords, nLevels, nTokens = len(sentence), len(sentence) * 2, len(tokens)
lengths = [nWords] + [nWords - math.floor((i + 1) / 2) + 1 for i in range(1, nLevels)]

# c[i][j] is the cost of the jth word at the ith level
c = VarArray(size=[nLevels, nWords], dom=lambda i, j: costs if (i == 0 or i % 2 == 1) and j < lengths[i] else {0})

# l[i][j] is the label of the jth word at the ith level
l = VarArray(size=[nLevels, nWords], dom=lambda i, j: range(nTokens + 1) if j < lengths[i] else {0})

# a[i][j] is the arity of the jth word at the ith level
a = VarArray(size=[nLevels, nWords], dom=lambda i, j: range(maxArity + 1) if i % 2 == 1 and j < lengths[i] else {0})

# x[i][j] is the index of the jth word at the ith level
x = VarArray(size=[nLevels, nWords], dom=lambda i, j: range(lengths[i]) if 0 < i and i % 2 == 0 and j < lengths[i] else {0})

s = VarArray(size=nLevels - 2, dom=lambda i: range(lengths[i + 1]))


def table_for(vector_length):
    arity = vector_length + 2
    table = {tuple([ANY] * (arity - 1) + [0])}
    for i in range(vector_length):
        for j in range(1, len(tokens) + 1):
            t = [ANY] * arity
            t[0] = i
            t[i + 1] = j
            t[arity - 1] = j
            table.add(tuple(t))
    return table


def table_for_grammar(n):
    return {tuple(ANY if v == 2147483646 else v for v in t) for t in grammar[n]}


def predicate(i, j):
    r = range(1 if i != 0 and j == lengths[i] - 1 else 0, min(j + 1, maxArity))
    return xor(*([l[i][j] == 0] + [a[i + 1][j - k] >= k + 1 for k in r]))


satisfy(
    [Count(l[i][:lengths[i]], value=0) == s[i - 1] for i in range(1, nLevels - 1)],

    [s[i - 1] == s[i] for i in range(1, nLevels - 1, 2)],

    # on row 0, costs are 0
    [c[0][j] == 0 for j in range(nWords)],

    # on row 0, the jth label is the jth word of the sentence
    [l[0][j] == sentence[j] for j in range(nWords)],

    # on column 0, labels are 0
    [l[i][0] > 0 for i in range(1, nLevels)],

    [a[p][0] > 0 for p in range(1, nLevels, 2)],

    [a[i][j] <= lengths[i - 1] - j for i in range(1, nLevels, 2) for j in range(1, nWords) if j < lengths[i] and j + maxArity > lengths[i - 1]],

    [
        (
            x[i][0] == 0,
            l[i][0] == l[i - 1][0]
        ) for i in range(2, nLevels, 2)
    ],

    [(x[i][j], l[i - 1][:lengths[i - 1]], l[i][j]) in table_for(lengths[i - 1]) for i in range(2, nLevels, 2) for j in range(1, lengths[i])],

    [
        (
            x[i][j] >= j,
            If(l[i][j] == 0, Then=x[i][j] == lengths[i] - 1),
            If(l[i][j] > 0, Then=x[i][j] > x[i][j - 1]),
            If(l[i][j - 1] == 0, Then=l[i][j] == 0)
        ) for i in range(2, nLevels, 2) for j in range(1, lengths[i])
    ],

    # grammar a
    [
        (
            (l[i][j] == 0) == (a[i][j] == 0),
            (a[i][j], l[i][j], l[i - 1][j: j + k], c[i][j]) in table_for_grammar(k)
        ) for i in range(1, nLevels, 2) for j in range(lengths[i]) if (k := min(lengths[i - 1] - j, maxArity),)
    ],

    [predicate(i, j) for i in range(0, nLevels, 2) for j in range(nWords) if j < lengths[i]],

    l[2 * maxHeight][1] == 0 if 0 < maxHeight and 2 * maxHeight < len(l) else None
)

minimize(
    Sum(c)
)
