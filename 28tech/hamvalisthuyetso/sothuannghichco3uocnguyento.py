from math import *


def sothuannghich(n):
    m = 0
    o = n
    while (n):
        m = m * 10 + n % 10
        n //= 10
    if (m == o):
        return True
    return False


def ok(n):
    dem = 0
    for i in range(2, isqrt(n) + 1):
        if (n % i == 0):
            dem += 1
            while (n % i == 0):
                n //= i
    if (n != 1):
        dem += 1
    return dem >= 3


if __name__ == '__main__':
    n, m = map(int, input().split())
    okk = 0
    for i in range(n, m + 1):
        if (ok(i) == True and sothuannghich(i) == True):
            print(i, end=' ')
            okk += 1
    if (okk == 0):
        print("-1")
