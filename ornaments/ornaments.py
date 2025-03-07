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
    while True:
        line: str = input().strip()
        # radius, distance, percent
        r, h, s = map(int, line.split())

        if r == 0 and h == 0 and s == 0:
            break

        result = calculate_string_length(r, h, s)
        print(f"{result:.2f}")


if __name__ == "__main__":
    main()