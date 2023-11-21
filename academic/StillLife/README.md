# Problem StillLife
## Description
This is the [problem 032](https://www.csplib.org/Problems/prob032/) of the CSPLib:

This problem arises from the Game of Life, invented by John Horton Conway in the 1960s and popularized by Martin Gardner in his Scientific American columns.

Life is played on a squared board, considered to extend to infinity in all directions. Each square of the board is a cell,
which at any time during the game is either alive or dead. A cell has eight neighbours:

The configuration of live and dead cells at time t leads to a new configuration at time t+1 according to the rules of the game:

 - if a cell has exactly three living neighbours at time t, it is alive at time t+1
 - if a cell has exactly two living neighbours at time t it is in the same state at time t+1 as it was at time t
 - otherwise, the cell is dead at time t+1


### Example

Here is a solution for a 3x3 still-life with 6 live cells (the optimum). (source from CSPlib):

![Life3](https://www.csplib.org/Problems/prob032/assets/life3.jpg)

## Data
A tuple \[n,m], where n is the number of rows and m the number of columns.

## Model(s)


There are two variants, a classical one and a "wastage" one.

  constraints: [Extension](http://pycsp.org/documentation/constraints/Extension), [Intension](http://pycsp.org/documentation/constraints/Intension), [Sum](http://pycsp.org/documentation/constraints/Sum)


## Command Line


```
python StillLife.py
python StillLife.py -data=[7,7]
python StillLife.py -data=[7,7] -variant=wastage
```

## Tags
 academic csplib