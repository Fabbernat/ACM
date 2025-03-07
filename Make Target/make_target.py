def main():
    N = int(input().strip())

    # ures grid
    target = [['.'] * N for _ in range(N)]

    # j = N + 1 - i
    for i in range(N):
        j = N - i

        # Fill from (i,i) to (j-1, j-1)
        for x in range(i, j):
            for y in range(i, j):
                target[x][y] = '#' if i % 2 == 0 else '.'

    for row in target:
        print(''.join(row))


if __name__ == "__main__":
    main()
