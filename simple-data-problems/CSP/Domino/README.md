
# Problem Domino

## Description
This problem is described in "[Making AC3 an optimal algorithm](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.103.1730&rep=rep1&type=pdf)" 
by Zhang and Yap, IJCAI 2001. Informally the Domino problem is an undirected constraint graph with a cycle and a trigger constraint.

### Example


## Data
A couple (n,d), where n is the number of variables and d the size of the domain.
## Model(s)


There are two variants, one if  constraints in intension, the other with constraints in extension.

*Involved Constraints*: [AllEqual](https://pycsp.org/documentation/constraints/AllEqual/), [Intension](https://pycsp.org/documentation/constraints/Intension/),
[Extension](https://pycsp.org/documentation/constraints/Extension/).



## Command Line


```shell
  python3 Domino.py
  python3 Domino.py -data=[300,300]
  python3 Domino.py -data=[300,300] -variant=table
  ```

## Some Results

| Data       | Number of Solutions |
|------------|-------------------|
| \[300,300] | 1 | 
| \[400,400] | 1 | 