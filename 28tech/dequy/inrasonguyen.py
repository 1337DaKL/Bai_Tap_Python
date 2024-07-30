def traiquaphai(n):
    if (n // 10 == 0):
        print(n, end=" ")
    else:
        m = n % 10
        traiquaphai(n // 10)
        print(m, end=" ")


def phaiquartrai(n):
    if (n // 10 == 0):
        print(n, end=' ')
    else:
        print(n % 10, end=' ')
        phaiquartrai(n // 10)


if __name__ == '__main__':
    n = int(input())
    traiquaphai(n)
    print()
    phaiquartrai(n)
