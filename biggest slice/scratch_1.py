import math
import sys
input = sys.stdin.readline

def calculate_largest_slice(r, n, theta_degrees, theta_minutes, theta_seconds):
    # Convert angle to radians
    theta_total_seconds = theta_degrees * 3600 + theta_minutes * 60 + theta_seconds
    theta_radians = (theta_total_seconds / 3600) * (math.pi / 180)

    # Calculate pizza area
    pizza_area = math.pi * r * r

    # First, check if we go around the entire pizza
    full_rotations = (n * theta_radians) / (2 * math.pi)

    # If we don't make a full circle, the largest slice is the full pizza
    if full_rotations < 1:
        return pizza_area

    # Calculate the effective number of slices
    gcd_value = math.gcd(n, round(360 * 3600 / theta_total_seconds))
    effective_slices = n // gcd_value

    # The largest slice area is a proportional part of the total area
    largest_slice = pizza_area / effective_slices

    return largest_slice


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        r, n, theta_degrees, theta_minutes, theta_seconds = map(int, input().strip().split())

        result = calculate_largest_slice(r, n, theta_degrees, theta_minutes, theta_seconds)
        print(f"{result:.6f}")


if __name__ == "__main__":
    main()