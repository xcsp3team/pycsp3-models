# Problem SkillAllocation

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2020 Minizinc challenge.
No Licence was explicitly mentioned (MIT Licence is assumed).

## Data Example
  2w-1.json

## Model
  constraints: [Count](http://pycsp.org/documentation/constraints/Count), [Sum](http://pycsp.org/documentation/constraints/Sum)

## Execution
```
  python SkillAllocation.py -data=<datafile.json>
  python SkillAllocation.py -data=<datafile.dzn> -parser=SkillAllocation_ParserZ.py
```

## Links
  - https://www.minizinc.org/challenge2020/results2020.html

## Tags
  realistic, mzn20
