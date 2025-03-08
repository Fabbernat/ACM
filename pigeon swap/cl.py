import sys

input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())

    # Initialize: pigeon i is in nest i
    pigeon_to_nest = {i: i for i in range(1, N + 1)}
    nest_to_pigeons = {i: [i] for i in range(1, N + 1)}

    results = []

    for _ in range(Q):
        op = list(map(int, input().split()))

        if op[0] == 1:  # Type 1: Move pigeon a to nest b
            a, b = op[1], op[2]
            current_nest = pigeon_to_nest[a]

            # Remove pigeon from current nest
            nest_to_pigeons[current_nest].remove(a)

            # Add pigeon to new nest
            nest_to_pigeons[b].append(a)

            # Update pigeon's location
            pigeon_to_nest[a] = b

        elif op[0] == 2:  # Type 2: Swap all pigeons between nests a and b
            a, b = op[1], op[2]

            # Swap the lists of pigeons in the two nests
            nest_to_pigeons[a], nest_to_pigeons[b] = nest_to_pigeons[b], nest_to_pigeons[a]

            # Update the locations for all affected pigeons
            for pigeon in nest_to_pigeons[a]:
                pigeon_to_nest[pigeon] = a

            for pigeon in nest_to_pigeons[b]:
                pigeon_to_nest[pigeon] = b

        elif op[0] == 3:  # Type 3: Report the nest of pigeon a
            a = op[1]
            results.append(pigeon_to_nest[a])

    # Print results
    for result in results:
        print(result)


if __name__ == '__main__':
    main()