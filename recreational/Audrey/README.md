# Problem Audrey

Little Problem given by Audrey at n-Side (see problem in OscaR).

Based on a little game I used to play in high school when I was getting bored in the classroom...
Draw a ten cells by ten cells board.
The purpose is to fill in all cells with numbers from 0 to 99.
You start by writing 0 in whatever cell.
From there on, you need to write the 1 by moving around in one of the following ways:
  - Move by 3 cells horizontally or vertically
  - Or move by 2 cells diagonally
Then, starting from the 1, you need to write the 2 using the same permitted moves, and so on.

The problem can be generalized for any order n.

## Data
  An integer n, the number of cells

## Model
  constraints: [Circuit](http://pycsp.org/documentation/constraints/Circuit)

## Execution
```
  python Audrey.py -data=number
  python Audrey.py -data=number -variant=display1
  python Audrey.py -data=number -variant=display2
```

## Tags
  academic, recreational
