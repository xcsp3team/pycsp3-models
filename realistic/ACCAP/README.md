# Problem ACCAP

Airport Check-in Counter Allocation Problem (ACCAP) with fixed opening/closing times.

Airports have a specific set of check-in counters available for common use by multiple airlines throughout the day.
Airlines have predetermined start and end times for their flight check-in operations before their departure times.
Each flight operates within a fixed time interval during which the check-in must remain open.
Given the number of airlines, their respective flights, the start times for check-in (x),
the required counter capacity (requirement), and the check-in duration (duration),
the objective is to allocate flights (check-ins) to counters (y, indicating the tarting counter index) in a way
that minimizes the maximum number of counters used throughout the day (z).
Simultaneously, the goal is to cluster flights from the same airline together
in the same check-in area, achieving this by minimizing the sum of the total distances (d)
between the counters of each pair of flights from the same airline.

The model, below, is close to (can be seen as the close translation of) the one submitted to the 2019/2022 Minizinc challenges.
No Licence was explicitly mentioned (MIT Licence assumed).

## Data
  03.json

## Model
 Two variants manage in a slightly different manner the way distances are computed:
  - a main variant involving logical constraints
  - a variant 'sum' forcing the presence of Sum constraints

  constraints: [NoOverlap](http://pycsp.org/documentation/constraints/NoOverlap), [Sum](http://pycsp.org/documentation/constraints/Sum)

## Execution
  - python ACCAP.py -data=<datafile.json>
  - python ACCAP.py -data=<datafile.json> -variant=sum
  - python ACCAP.py -data=<datafile.dzn> -parser=ACCAP_ParserZ.py

## Links
  - https://www.minizinc.org/challenge2022/results2022.html

## Tags
  realistic, mzn19, mzn22
