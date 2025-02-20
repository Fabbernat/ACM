from collections import defaultdict
import sys

input = sys.stdin.read


def max_profit_per_test_case(n, bottles):
    brand_costs = defaultdict(list)

    # Group bottles by brand with their respective costs
    for b, c in bottles:
        brand_costs[b].append(c)

    # Sum the highest costs up to the number of shelves (n)
    total_profit = 0
    all_brand_profits = []

    for costs in brand_costs.values():
        # Sort costs for each brand in descending order and get the top `n` elements
        costs.sort(reverse=True)
        brand_profit = sum(costs[:n])
        all_brand_profits.append(brand_profit)

    # Sort all possible profits and sum up the top `n`
    all_brand_profits.sort(reverse=True)
    total_profit = sum(all_brand_profits[:n])

    return total_profit


# Read input
data = input().split()
t = int(data[0])
index = 1
results = []

# Process each test case
for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2

    bottles = []
    for _ in range(k):
        b = int(data[index])
        c = int(data[index + 1])
        bottles.append((b, c))
        index += 2

    # Calculate maximum profit for the current test case
    result = max_profit_per_test_case(n, bottles)
    results.append(result)

# Print all results for each test case
sys.stdout.write("\n".join(map(str, results)) + "\n")
