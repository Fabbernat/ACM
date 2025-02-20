import sys


def john_wins(eminems):
    total_eminems = sum(eminems)
    if total_eminems == 1:
        return False

    xor_sum = 0
    for count in eminems:
        xor_sum ^= count

    return xor_sum != 0


def read_lines(T):
    lines = []
    for _ in range(T * 2):
        lines.append(sys.stdin.readline().strip())
    return lines


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        _ = int(sys.stdin.readline().strip())
        eminems = list(map(int, sys.stdin.readline().strip().split()))
        print("John" if john_wins(eminems) else "Brother")