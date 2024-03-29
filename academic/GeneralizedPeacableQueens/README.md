# Problem GeneralizedPeacableQueens

Generalized Peaceable Queens.

On a board, put the maximal number of black and white queens while having no attack from opposing sides.
The number of black queens must be equal to the number of white queens.

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2022 Minizinc challenge.
The MZN model was proposed by Hendrik 'Henk' Bierlee, under the MIT Licence.

## Data
  two integers (n,q)

## Model
  constraints: [Cardinality](http://pycsp.org/documentation/constraints/Cardinality), [Lex](http://pycsp.org/documentation/constraints/Lex), [Precedence](http://pycsp.org/documentation/constraints/Precedence), [Regular](http://pycsp.org/documentation/constraints/Regular)

## Execution
```
  python GeneralizedPeacableQueens.py -data=[number,number]
```

## Links
  - https://oeis.org/A250000
  - https://link.springer.com/chapter/10.1007/978-3-540-24664-0_19
  - https://www.minizinc.org/challenge2022/results2022.html

## Tags
  academic, mzn22
