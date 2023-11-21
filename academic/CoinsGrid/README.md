# Problem CoinsGrid
## Description
This problem can be found in [Constraint Solving and Planning with Picat](https://link.springer.com/book/10.1007/978-3-319-25883-6), page 43:


In a quadratic grid (or a larger chessboard) with 31 ×31 cells, one should place coins in
such a way that the following conditions are fulfilled:
 - In each row exactly 14 coins must be placed.
 - In each column exactly 14 coins must be placed.
 - The sum of the quadratic horizontal distance from the main diagonal of all cells containing a coin must be as small as possible.
 - In each cell at most one coin can be placed.

### Example

The optimum for a grid of size 8 and 4 coins to put in each row and column.

```
     1 1 1 1 0 0 0 0
     1 1 1 1 0 0 0 0
     1 1 1 1 0 0 0 0
     1 1 1 1 0 0 0 0
     0 0 0 0 1 1 1 1
     0 0 0 0 1 1 1 1
     0 0 0 0 1 1 1 1
     0 0 0 0 1 1 1 1
```

## Data

A couple \[n,c], where n is the size of the grid and c is the number of coins (by default \[31,14])

## Model(s)


  constraints: [Sum](http://pycsp.org/documentation/constraints/Sum)


## Command Line

```
python CoinsGrid.py
python CoinsGrid.py -data=[10,4]
```

## Tags
 academic