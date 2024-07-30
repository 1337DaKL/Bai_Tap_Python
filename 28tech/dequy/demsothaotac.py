def dem(n):
    if (n == 1):
        return 0
    tt1, tt2, tt3 = 10 ** 9, 10**9, 10 ** 9
    if (n % 2 == 0):
        tt1 = 1 + dem(n // 2)
    if (n % 3 == 0):
        tt2 = 1 + dem(n // 3)
    if (n > 1):
        tt3 = 1 + dem(n - 1)
    return min(tt1, tt2, tt3)


if __name__ == '__main__':
    n = int(input())
    print(dem(n))
