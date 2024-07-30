def tong(n):
    if (n == 1):
        return 1
    return 1 / n + tong(n - 1)


if __name__ == '__main__':
    n = int(input())
    print('%.3f' % tong(n))
