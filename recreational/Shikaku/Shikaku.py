"""
A logic puzzle. See "Shikaku as a Constraint Problem" by Helmut Simonis.

## Data Example
  grid01.json

## Model
  constraints: Table

## Execution:
  python3 Shikaku.py -data=<datafile.json>

## Links
 - https://en.wikipedia.org/wiki/Shikaku

## Tags
  recreational
"""

from pycsp3 import *

nRows, nCols, rooms = data
nRooms = len(rooms)


def no_overlapping(i, j):
    leftmost = i if rooms[i].col <= rooms[j].col else j
    rightmost = j if leftmost == i else i
    p = r[leftmost] <= l[rightmost]
    if rooms[leftmost].row == rooms[rightmost].row:
        return p
    if rooms[leftmost].row > rooms[rightmost].row:
        return p | (t[leftmost] >= b[rightmost])
    return p | (b[leftmost] <= t[rightmost])


# l[i] is the position of the left border of the ith room
l = VarArray(size=nRooms, dom=range(nCols + 1))

# r[i] is the position of the right border of the ith room
r = VarArray(size=nRooms, dom=range(nCols + 1))

# t[i] is the position of the top border of the ith room
t = VarArray(size=nRooms, dom=range(nRows + 1))

# b[i] is the position of the bottom border of the ith room
b = VarArray(size=nRooms, dom=range(nRows + 1))

satisfy(
    # each room must be surrounded by its borders
    [
        (
            l[i] <= col,
            r[i] > col,
            t[i] <= row,
            b[i] > row
        ) for i, (row, col, _) in enumerate(rooms)
    ],

    # respecting the surface of each room
    [(r[i] - l[i]) * (b[i] - t[i]) == v for i, (_, _, v) in enumerate(rooms)],

    # rooms must not overlap
    [no_overlapping(i, j) for i, j in combinations(nRooms, 2)]
)

""" Comments
1) it is also possible to write (but this is less compact):
 [l[i] <= rooms[i].col for i in range(nRooms)],
 [r[i] > rooms[i].col for i in range(nRooms)],
 [t[i] <= rooms[i].row for i in range(nRooms)],
 [b[i] > rooms[i].row for i in range(nRooms)],
"""
