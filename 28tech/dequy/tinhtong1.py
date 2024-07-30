from math import *


def tong(n):
    if (n == 1):
        return n
    return n + tong(n - 1)


if __name__ == '__main__':
    n = int(input())
    print(tong(n))
