"""
The rectangle (square) packing problem consists of squares (bowes)
to be put in an enclosing rectangle (container) without overlapping of the squares.


## Data
  perfect-001.json

## Model
  constraints: NoOverlap

## Execution
  python RectPacking.py -data=<datafile.json>

## Links
  - https://link.springer.com/chapter/10.1007/978-3-540-85958-1_4

## Tags
  realistic
"""

from pycsp3 import *

width, height = data.container
boxes = data.boxes
nBoxes = len(boxes)

# x[i] is the x-coordinate where is put the ith rectangle
x = VarArray(size=nBoxes, dom=range(width))

# y[i] is the y-coordinate where is put the ith rectangle
y = VarArray(size=nBoxes, dom=range(height))

satisfy(
    # unary constraints on x
    [x[i] + boxes[i].width <= width for i in range(nBoxes)],

    # unary constraints on y
    [y[i] + boxes[i].height <= height for i in range(nBoxes)],

    # no overlap on boxes
    NoOverlap(origins=[(x[i], y[i]) for i in range(nBoxes)], lengths=boxes),

    # tag(symmetry-breaking)
    [x[-1] <= (width - boxes[-1].width) // 2, y[-1] <= x[-1]] if width == height else None
)

""" Comments
1) even if elements of boxes are named tuples, one can write length=boxes instead of lengths=[(w, h) for (w, h) in boxes]
2) see also CP papers on short supports
"""
