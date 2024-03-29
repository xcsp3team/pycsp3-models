# Problem MultiKnapsack

The Multi dimensional knapsack problem was originally proposed as an optimization problem by the OR community.
Here, it is the feasibility version, as used, e.g., in (Refalo, CP 2004) and (Pesant et al., JAIR 2012).

## Data Example
  OR05x100-25-1.json

## Model
  constraints: [Sum](http://pycsp.org/documentation/constraints/Sum)

## Execution
```
  python MultiKnapsack.py -data=<datafile.json>
  python MultiKnapsack.py -data=<datafile.txt> -parser=MultiKnapsack_Parser.py
```

## Links
  - https://www.researchgate.net/publication/271198281_Benchmark_instances_for_the_Multidimensional_Knapsack_Problem

## Tags
 recreational

<br />

## _Alternative Model(s)_

#### MultiKnapsack_z1.py
 - constraints: [Sum](http://pycsp.org/documentation/constraints/Sum)
 - tags: crafted, mzn14
#### MultiKnapsack_z2.py
 - constraints: [Knapsack](http://pycsp.org/documentation/constraints/Knapsack), [Sum](http://pycsp.org/documentation/constraints/Sum)
 - tags: crafted, mzn15, mzn19
