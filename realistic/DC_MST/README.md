# Problem DC_MST

Diameter Constrained Minimum Spanning Tree.
Given an undirected graph G=(V,E) and an integer k find a spanning tree of G of minimum cost such that its diameter is not greater than k.

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2016/2022 Minizinc challenges.
No Licence was explicitly mentioned (MIT Licence assumed).

## Data Example
  s-v20-a50-d4.json

## Model
  constraints: [Sum](http://pycsp.org/documentation/constraints/Sum)

## Execution
```
  python DC_MST.py -data=<datafile.json>
  python DC_MST.py -data=<datafile.dzn> -parser=DC_MST_ParserZ.py
```

## Links
  - https://www.minizinc.org/challenge2022/results2022.html

## Tags
  realistic, mzn16, mzn22
