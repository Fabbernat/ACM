import math


def solve_logo1():
    def normalize_angle(angle):
        return angle % 360

    def get_final_position(commands, test_value):
        x, y = 0, 0
        angle = 0

        for cmd, val in commands:
            value = test_value if val == '?' else int(val)

            if cmd == 'fd':
                x += value * math.cos(math.radians(angle))
                y += value * math.sin(math.radians(angle))
            elif cmd == 'bk':
                x -= value * math.cos(math.radians(angle))
                y -= value * math.sin(math.radians(angle))
            elif cmd == 'lt':
                angle = normalize_angle(angle + value)
            elif cmd == 'rt':
                angle = normalize_angle(angle - value)

        return x, y, angle

    t = int(input())
    for _ in range(t):
        n = int(input())
        commands = []
        missing_idx = 0

        for i in range(n):
            cmd, val = input().split()
            if val == '?':
                missing_idx = i
            commands.append((cmd, val))

        missing_cmd = commands[missing_idx][0]

        if missing_cmd in ['fd', 'bk']:
            left, right = 0, 10000
            while left < right:
                mid = (left + right) // 2
                x, y, _ = get_final_position(commands, mid)
                dist = x * x + y * y

                if abs(dist) < 1e-6:
                    print(mid)
                    break
                elif dist > 0:
                    left = mid + 1
                else:
                    right = mid - 1
        else:  # lt or rt
            for angle in range(360):
                x, y, final_angle = get_final_position(commands, angle)
                if abs(x) < 1e-6 and abs(y) < 1e-6:
                    print(angle)
                    break


# Solution 2: Using state tracking
def solve_logo2():
    def normalize_angle(angle):
        return angle % 360

    class TurtleState:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.angle = 0

        def move(self, dist, forward=True):
            mult = 1 if forward else -1
            self.x += dist * mult * math.cos(math.radians(self.angle))
            self.y += dist * mult * math.sin(math.radians(self.angle))

        def turn(self, angle, left=True):
            mult = 1 if left else -1
            self.angle = normalize_angle(self.angle + angle * mult)

        def distance_from_start(self):
            return math.sqrt(self.x * self.x + self.y * self.y)

    t = int(input())
    for _ in range(t):
        n = int(input())
        commands = []
        turtle = TurtleState()
        missing_cmd = None
        missing_idx = 0

        for i in range(n):
            cmd, val = input().split()
            if val == '?':
                missing_cmd = cmd
                missing_idx = i
            else:
                val = int(val)
                if cmd == 'fd':
                    turtle.move(val)
                elif cmd == 'bk':
                    turtle.move(val, False)
                elif cmd == 'lt':
                    turtle.turn(val)
                elif cmd == 'rt':
                    turtle.turn(val, False)
            commands.append((cmd, val))

        if missing_cmd in ['fd', 'bk']:
            # Binary search for distance
            left, right = 0, 10000
            while left < right:
                mid = (left + right) // 2
                test_turtle = TurtleState()
                for i, (cmd, val) in enumerate(commands):
                    if i == missing_idx:
                        if missing_cmd == 'fd':
                            test_turtle.move(mid)
                        else:
                            test_turtle.move(mid, False)
                    elif cmd == 'fd':
                        test_turtle.move(int(val))
                    elif cmd == 'bk':
                        test_turtle.move(int(val), False)
                    elif cmd == 'lt':
                        test_turtle.turn(int(val))
                    elif cmd == 'rt':
                        test_turtle.turn(int(val), False)

                dist = test_turtle.distance_from_start()
                if abs(dist) < 1e-6:
                    print(mid)
                    break
                elif dist > 0:
                    left = mid + 1
                else:
                    right = mid - 1
        else:  # lt or rt
            # Try all possible angles
            for angle in range(360):
                test_turtle = TurtleState()
                for i, (cmd, val) in enumerate(commands):
                    if i == missing_idx:
                        if missing_cmd == 'lt':
                            test_turtle.turn(angle)
                        else:
                            test_turtle.turn(angle, False)
                    elif cmd == 'fd':
                        test_turtle.move(int(val))
                    elif cmd == 'bk':
                        test_turtle.move(int(val), False)
                    elif cmd == 'lt':
                        test_turtle.turn(int(val))
                    elif cmd == 'rt':
                        test_turtle.turn(int(val), False)

                if test_turtle.distance_from_start() < 1e-6:
                    print(angle)
                    break


# Solution 3: Using angle calculations
def solve_logo3():
    def normalize_angle(angle):
        return angle % 360

    def get_angle_diff(start_angle, end_angle, is_left):
        diff = end_angle - start_angle
        if is_left:
            if diff < 0:
                diff += 360
        else:
            if diff > 0:
                diff = 360 - diff
            else:
                diff = -diff
        return normalize_angle(diff)

    t = int(input())
    for _ in range(t):
        n = int(input())
        x = y = 0
        angle = 0
        commands = []
        missing_idx = 0

        for i in range(n):
            cmd, val = input().split()
            if val == '?':
                missing_idx = i
            commands.append((cmd, val))

        # Calculate position and angle before missing command
        for i in range(missing_idx):
            cmd, val = commands[i]
            val = int(val)
            if cmd == 'fd':
                x += val * math.cos(math.radians(angle))
                y += val * math.sin(math.radians(angle))
            elif cmd == 'bk':
                x -= val * math.cos(math.radians(angle))
                y -= val * math.sin(math.radians(angle))
            elif cmd == 'lt':
                angle = normalize_angle(angle + val)
            elif cmd == 'rt':
                angle = normalize_angle(angle - val)

        missing_cmd = commands[missing_idx][0]
        if missing_cmd in ['fd', 'bk']:
            # Calculate required distance
            target_x = target_y = 0
            temp_angle = angle

            # Calculate where we need to end up
            for i in range(missing_idx + 1, n):
                cmd, val = commands[i]
                val = int(val)
                if cmd == 'fd':
                    target_x -= val * math.cos(math.radians(temp_angle))
                    target_y -= val * math.sin(math.radians(temp_angle))
                elif cmd == 'bk':
                    target_x += val * math.cos(math.radians(temp_angle))
                    target_y += val * math.sin(math.radians(temp_angle))
                elif cmd == 'lt':
                    temp_angle = normalize_angle(temp_angle + val)
                elif cmd == 'rt':
                    temp_angle = normalize_angle(temp_angle - val)

            # Calculate required distance
            required_dist = math.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
            print(round(required_dist))
        else:  # lt or rt
            target_angle = angle
            for i in range(missing_idx + 1, n):
                cmd, val = commands[i]
                val = int(val)
                if cmd == 'lt':
                    target_angle = normalize_angle(target_angle + val)
                elif cmd == 'rt':
                    target_angle = normalize_angle(target_angle - val)

            # Try all possible angles
            for test_angle in range(360):
                temp_angle = angle
                if missing_cmd == 'lt':
                    temp_angle = normalize_angle(temp_angle + test_angle)
                else:
                    temp_angle = normalize_angle(temp_angle - test_angle)

                # Continue with remaining commands
                x_test = x
                y_test = y
                for i in range(missing_idx + 1, n):
                    cmd, val = commands[i]
                    val = int(val)
                    if cmd == 'fd':
                        x_test += val * math.cos(math.radians(temp_angle))
                        y_test += val * math.sin(math.radians(temp_angle))
                    elif cmd == 'bk':
                        x_test -= val * math.cos(math.radians(temp_angle))
                        y_test -= val * math.sin(math.radians(temp_angle))
                    elif cmd == 'lt':
                        temp_angle = normalize_angle(temp_angle + val)
                    elif cmd == 'rt':
                        temp_angle = normalize_angle(temp_angle - val)

                if abs(x_test) < 1e-6 and abs(y_test) < 1e-6:
                    print(test_angle)
                    break


if __name__ == "__main__":
    # Choose which solution to run
    solve_logo1()  # Can change to solve_logo1() or solve_logo2()