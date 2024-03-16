"""

## Data
  04-04-0.json

## Model
  constraints: Maximum, NoOverlap

## Execution
  - python SchedulingFS.py -data=<datafile.json>
  - python SchedulingFS.py -data=<datafile.txt> -parser=SchedulingFS_Parser.py

## Links
  - https://en.wikipedia.org/wiki/Flow_shop_scheduling

## Tags
  realistic, notebook
"""

from pycsp3 import *

durations = data  # durations[i][j] is the duration of operation/machine j for job i
horizon = sum(sum(t) for t in durations) + 1
n, m = len(durations), len(durations[0])

# s[i][j] is the start time of the jth operation for the ith job
s = VarArray(size=[n, m], dom=range(horizon))

satisfy(
    # operations must be ordered on each job
    [Increasing(s[i], lengths=durations[i]) for i in range(n)],

    # no overlap on resources
    [
        NoOverlap(
            origins=s[:, j],
            lengths=durations[:, j]
        ) for j in range(m)
    ]
)

minimize(
    # minimizing the makespan
    Maximum(s[i][-1] + durations[i][-1] for i in range(n))
)
