import math
import sys
from typing import Any

input = sys.stdin.readline

def normalize_degree(degree: int | float) -> int | Any:
    return (degree % 360 + 360) % 360

def set_degree(degree:float, change)->int:
    while degree < 0:
        degree += 360
    while degree > 359:
        degree -= 360
    return degree

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dist_x : float = 0
        dist_y : float = 0
        degree : float = 0

        # default value, lehet barmelyik
        missing_command = 'fd'

        commands = []

        for _ in range(n):
            command, argument = input().strip().split(' ')
            commands.append((command, argument))

        for command, argument in commands:
            if argument == '?':
                missing_command = command
                continue

            value = int(argument)
            if command == 'lt':
                degree = normalize_degree(degree - value)
            elif command == 'rt':
                degree = normalize_degree(degree + value)
            elif command == 'fd':
                dist_x += value * math.cos(math.radians(degree))
                dist_y += value * math.sin(math.radians(degree))
            elif command == 'bd':
                dist_x -= value * math.cos(math.radians(degree))
                dist_y -= value * math.sin(math.radians(degree))

        if missing_command in ['fd', 'bd']:
            missing_argument = round(math.sqrt(dist_x ** 2 + dist_y ** 2))
            if missing_command == 'bd':
                missing_argument = -missing_argument
        else:
            missing_argument = round(math.degrees(math.atan2(dist_y, dist_x)))
            missing_argument = normalize_degree(missing_argument)

        print(missing_argument)

if __name__ == "__main__":
    main()