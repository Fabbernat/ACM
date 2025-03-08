import sys


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

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
            # Instead of directly setting parent, use find and update
            root_b = dsu.find(b)
            dsu.parent[a] = root_b

        elif op[0] == 2:
            a, b = op[1], op[2]
            dsu.union(a, b)  # Merge two nests

        else:
            a = op[1]
            results.append(str(dsu.find(a)))

    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    main()