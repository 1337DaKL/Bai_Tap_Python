def traisangphai(a, n):
    if n == 1:
        print(a[0], end=' ')
    else:
        b = a[n - 1]
        traisangphai(a, n - 1)
        print(b, end=' ')


def phaisangtrai(a, n):
    if (n == 1):
        print(a[0], end=" ")
    else:
        print(a[n - 1], end=" ")
        phaisangtrai(a, n - 1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    traisangphai(a, n)
    print()
    phaisangtrai(a, n)
