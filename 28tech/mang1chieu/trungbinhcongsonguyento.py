from math import *


def kiemtrasonguyento(n):
    if n <= 0:
        return False
    for i in range(2, isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return n > 1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    tong = 0
    dem = 0
    for i in range(0, len(a), 1):
        if kiemtrasonguyento(a[i]):
            dem += 1
            tong += a[i]
    print('%.3f' % (tong / dem))
