# Problem SteinerSystems

From WikiPedia: "A Steiner system with parameters t, k, n, written S(t,k,n), is an n-element set S
together with a set of k-element subsets of S (called blocks) with the property
that each t-element subset of S is contained in exactly one block.
In an alternate notation for block designs, an S(t,k,n) would be a t-(n,k,1) design."

## Data
  Three integers (t,k,n)

## Model
  constraints: [Count](http://pycsp.org/documentation/constraints/Count), [Lex](http://pycsp.org/documentation/constraints/Lex), [Sum](http://pycsp.org/documentation/constraints/Sum)

## Execution
```
  python SteinerSystems -data=[number,number,number]
```

## Links
  - https://en.wikipedia.org/wiki/Steiner_system
  - https://www.minizinc.org/challenge2021/results2021.html

## Tags
  academic, mzn21
