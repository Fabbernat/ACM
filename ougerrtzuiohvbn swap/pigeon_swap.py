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
        for i in range(Q):
            curr_ops = (map(int, (input().strip().split())))
            operations[i] = curr_ops

        print(f'{nest_number for nestnuber in sorted(operations[i]) for operation in operations}')


if __name__ == '__main__':
    main()