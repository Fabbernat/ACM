import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().strip().split()))

    for i in range(1, N):
        if A[i - 1] >= A[i]:
            print('No')
            exit(0)
    print('Yes')
    exit(0)

if __name__ == '__main__':
    main()