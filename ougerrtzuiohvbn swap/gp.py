import sys


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        # Iterative approach to avoid recursion
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        # Path compression (optional, but improves efficiency)
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x

        return root

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            if self.size[rootA] < self.size[rootB]:  # Union by size
                rootA, rootB = rootB, rootA
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())

    dsu = DSU(N)

    results = []

    for _ in range(Q):
        op = list(map(int, input().split()))

        if op[0] == 1:
            a, b = op[1], op[2]
            dsu.parent[a] = b  # Move pigeon `a` to nest `b`

        elif op[0] == 2:
            a, b = op[1], op[2]
            dsu.union(a, b)  # Merge two nests

        else:
            a = op[1]
            results.append(str(dsu.find(a)))

    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    main()
