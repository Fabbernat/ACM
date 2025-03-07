import math
import sys
from typing import Any

input = sys.stdin.readline

def normalize_angle(angle: int | float) -> int | Any:
    return angle % 360

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dist_x: int = 0
        dist_y: int = 0
        angle: int = 0
        commands = []
        missing_index = 0

        for i in range(n):
            command, argument = input().strip().split(' ')
            if argument == '?':
                missing_index = i
            commands.append((command, argument))

        for i in range(missing_index):
            command, argument = commands[i]
            argument = int(argument)
            if command == 'fd':
                dist_x += argument * math.cos(math.radians(angle))
                dist_y += argument * math.sin(math.radians(angle))
            elif command == 'bk':
                dist_x -= argument * math.cos(math.radians(angle))
                dist_y -= argument * math.sin(math.radians(angle))
            elif command == 'lt':
                angle = normalize_angle(angle + argument)
            elif command == 'rt':
                angle = normalize_angle(angle - argument)

        missing_command = commands[missing_index][0]
        if missing_command in ['fd', 'bk']:

            # szamitas
            target_x = target_y = 0
            temp_angle = angle

            # kiszamolja h hova kerul a teknos
            for i in range(missing_index + 1, n):
                command, argument = commands[i]
                argument = int(argument)
                if command == 'fd':
                    target_x -= argument * math.cos(math.radians(temp_angle))
                    target_y -= argument * math.sin(math.radians(temp_angle))
                elif command == 'bk':
                    target_x += argument * math.cos(math.radians(temp_angle))
                    target_y += argument * math.sin(math.radians(temp_angle))
                elif command == 'lt':
                    temp_angle = normalize_angle(temp_angle + argument)
                elif command == 'rt':
                    temp_angle = normalize_angle(temp_angle - argument)

            # szam 2
            required_dist = math.sqrt((dist_x - target_x) ** 2 + (dist_y - target_y) ** 2)
            print(round(required_dist))
        else:  # lt or rt
            target_angle = angle
            for i in range(missing_index + 1, n):
                command, argument = commands[i]
                argument = int(argument)
                if command == 'lt':
                    target_angle = normalize_angle(target_angle + argument)
                elif command == 'rt':
                    target_angle = normalize_angle(target_angle - argument)

            # brute force kiprobalunk minden iranyt
            for test_angle in range(360):
                temp_angle = angle
                if missing_command == 'lt':
                    temp_angle = normalize_angle(temp_angle + test_angle)
                else:
                    temp_angle = normalize_angle(temp_angle - test_angle)

                # folytatas
                x_test = dist_x
                y_test = dist_y
                for i in range(missing_index + 1, n):
                    command, argument = commands[i]
                    argument = int(argument)
                    if command == 'fd':
                        x_test += argument * math.cos(math.radians(temp_angle))
                        y_test += argument * math.sin(math.radians(temp_angle))
                    elif command == 'bk':
                        x_test -= argument * math.cos(math.radians(temp_angle))
                        y_test -= argument * math.sin(math.radians(temp_angle))
                    elif command == 'lt':
                        temp_angle = normalize_angle(temp_angle + argument)
                    elif command == 'rt':
                        temp_angle = normalize_angle(temp_angle - argument)

                if abs(x_test) < 1e-6 and abs(y_test) < 1e-6:
                    print(test_angle)
                    break


if __name__ == "__main__":
    main()
