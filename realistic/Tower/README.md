# Problem Tower

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2020/2022 Minizinc challenges.
The MZN model was proposed by Greame Gange, with a Licence that seems to be like the MIT Licence.

## Data Example
  070-070-15-070-04.json

## Model
  constraints: [MaximumArg](http://pycsp.org/documentation/constraints/MaximumArg), [Sum](http://pycsp.org/documentation/constraints/Sum)

## Execution
```
  python Tower.py -data=<datafile.json>
  python Tower.py -data=<datafile.dzn> -parser=Tower_ParserZ.py
```

## Links
  - https://www.minizinc.org/challenge2022/results2022.html

## Tags
  realistic, mzn20, mzn22
