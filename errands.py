import sys
import math
import itertools
from typing import Any

# faster input reading
input = sys.stdin.readline

#In Python, the maximum value of an integer is not fixed and can grow to the limit of the available memory. This is because Python 3 uses arbitrary-precision integers, meaning it can handle very large numbers without any special arrangements
INF = 1e18

# Euclidean distance between two points
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def travelling_salesman_problem(distance_matrix):
    n = len(distance_matrix)

    dp_cost = [[INF for _ in range(n)] for _ in range(1 << n)]

    dp_cost[1][0] = 0
    previous_location = [[0 for _ in range(n)] for _ in range(1 << n)]
    for subset in range(1 << n):
        for i in range(n):
            for j in range(n):
                if subset & (1 << j) == 0:
                    new_subset = subset + (1 << j)
                    dp_cost[new_subset][j], previous_location[new_subset][j] = min((dp_cost[subset][i] + distance_matrix[i][j], i),
                                             (dp_cost[new_subset][j], previous_location[new_subset][j]))
    optimal_tour = []

    last_location = n - 1

    state = (1 << n) - 1
    while last_location:
        next_location = previous_location[state][last_location]
        state -= 1 << last_location
        last_location = next_location
        optimal_tour.append(last_location)
    return optimal_tour[-2::-1]

def solve():
    locations = {}
    for _ in range(int(input())):
        line, x, y = input().split()
        locations[line] = complex(round(float(x) * 100000.0), round(float(y) * 100000.0))
    for line in sys.stdin:
        m: dict[str, int] = {'work': 0, **{e: i + 1 for i, e in enumerate(line.strip().split())}}

        line: Any = [*m]

        m['home'] = len(m)

        line.append('home')
        G = [[INF] * len(m) for _ in range(len(m))]
        for a in m:
            for b in m:
                if a < b: G[m[a]][m[b]] = G[m[b]][m[a]] = abs(locations[a] - locations[b])
        print(' '.join(line[i] for i in travelling_salesman_problem(G)))

if __name__ == "__main__":
    solve()