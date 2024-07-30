from math import *


def kiemtranguyento(n):
    for i in range(2, int(isqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return n > 1


def kiemtrathuan(n):
    if (kiemtranguyento(n) == False):
        return False
    tong = 0
    while (n):
        m = n % 10
        if (m != 2 and m != 3 and m != 5 and m != 7):
            return False
        tong += m
        n //= 10
    if (kiemtranguyento(tong) == False):
        return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    dem = 0
    for i in range(n, m + 1, 1):
        if (kiemtrathuan(i)):
            dem += 1
    print(dem)
