# Problem Soccer

Soccer Computational Problem (Position in Ranking Problem).

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2018/2020 Minizinc challenges.
The original MZN model was proposed by Robinson Duque, Alejandro Arbelaez, and Juan Francisco Díaz.
No Licence was explicitly mentioned (MIT Licence is assumed).

## Data Example
  22-12-22-5.json

## Model
  constraints: [AllDifferent](http://pycsp.org/documentation/constraints/AllDifferent), [Sum](http://pycsp.org/documentation/constraints/Sum), [Table](http://pycsp.org/documentation/constraints/Table)

## Execution
```
  python Soccer.py -data=<datafile.json>
  python Soccer.py -data=<datafile.dzn> -parser=Soccer_ParserZ.py
```

## Links
  - https://www.aimsciences.org/article/doi/10.3934/jimo.2018109
  - https://www.minizinc.org/challenge2020/results2020.html

## Tags
  realistic, mzn18, mzn20
