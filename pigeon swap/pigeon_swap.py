import math
import sys
from typing import Any

input = sys.stdin.readline

def calculate_string_length(r: float, h: float, s: int) -> int | float | Any:
    # szog kozeprol a tangens pontig
    theta = math.asin(r / h)

    # arc length
    straight_length = h * math.cos(theta)

    arc_length = r * (math.pi + 2 * theta)

    total_length = 2 * straight_length + arc_length

    total_length *= (1 + s / 100)

    return total_length


def main():
    N, Q = map(int, input().strip().split())
    operations = []
    for _ in range(Q):
        operations.append(list(map(int, input().strip().split())))

    results = []
    pigeon_to_nest = list(range(1, N + 1))
    nest_to_pigeons = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        nest_to_pigeons[i].append(i)

    def move_pigeon(pigeon, new_nest):
        current_nest = pigeon_to_nest[pigeon - 1]
        nest_to_pigeons[current_nest].remove(pigeon)
        pigeon_to_nest[pigeon - 1] = new_nest
        nest_to_pigeons[new_nest].append(pigeon)

    def swap_nests(nest1, nest2):
        pigeons1 = nest_to_pigeons[nest1].copy()
        pigeons2 = nest_to_pigeons[nest2].copy()
        for pigeon in pigeons1:
            move_pigeon(pigeon, nest2)
        for pigeon in pigeons2:
            move_pigeon(pigeon, nest1)

    for op in operations:
        if op[0] == 1:
            a, b = op[1], op[2]
            move_pigeon(a, b)
        elif op[0] == 2:
            a, b = op[1], op[2]
            swap_nests(a, b)
        else:
            a = op[1]
            results.append(pigeon_to_nest[a - 1])

    for result in results:
        print(result)