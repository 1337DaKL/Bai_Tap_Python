def tohop(n, k):
    if (k == 0):
        return 1
    if (n == 0):
        return 0
    return tohop(n - 1, k - 1) + tohop(n - 1, k)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(tohop(n, k))
