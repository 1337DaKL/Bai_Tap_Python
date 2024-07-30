from math import *


def kiemtrasonguyento(n):
    for i in range(2, int(isqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return n > 1


def tongchuso(n):
    tong = 0
    while (n):
        tong += (n % 10)
        n //= 10
    return tong


def kiemtratong(n):
    tong = tongchuso(n)
    tongsnt = 0
    for i in range(2, int(isqrt(n)) + 1, 1):
        if (n % i == 0):
            while (n % i == 0):
                tongsnt += tongchuso(i)
                n //= i
    if (n > 1):
        tongsnt += tongchuso(n)
    return tong == tongsnt


if __name__ == '__main__':
    n = int(input())
    if (kiemtrasonguyento(n) == False and kiemtratong(n)):
        print("YES")
    else:
        print("NO")
