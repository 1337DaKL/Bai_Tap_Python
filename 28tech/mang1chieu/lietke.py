from math import *


def kiemtrasonguyento(n):
    for i in range(2, isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return n > 1


def sothuannghich(n):
    tong = 0
    m = n
    while (n):
        tong = tong * 10 + n % 10
        n //= 10
    if tong == m:
        return True
    return False


def sochinhphuong(n):
    a = isqrt(n)
    if a * a == n:
        return True
    return False


def tongchuso(n):
    tong = 0
    while (n):
        tong += n % 10
        n //= 10
    if (kiemtrasonguyento(tong)):
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    dem1, dem2, dem3, dem4 = 0, 0, 0, 0
    for i in range(n):
        if kiemtrasonguyento(a[i]):
            dem1 += 1
        if sothuannghich(a[i]):
            dem2 += 1
        if sochinhphuong(a[i]):
            dem3 += 1
        if tongchuso(a[i]):
            dem4 += 1

    print(dem1, dem2, dem3, dem4, sep='\n')
