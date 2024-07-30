from math import *


def ham1(n):
    for i in range(2, isqrt(n) + 1):
        if (n % i == 0):
            return 0
    if (n > 1):
        return 1


def ham2(n):
    tong = 0
    while (n):
        tong += n % 10
        n //= 10
    return tong


def ham3(n):
    tong = 0
    while (n):
        m = n % 10
        if (m % 2 == 0):
            tong += m
        n //= 10
    return tong


def ham4(n):
    tong = 0
    while (n):
        m = n % 10
        if (m == 2 or m == 3 or m == 5 or m == 7):
            tong += m
        n //= 10
    return tong


def ham5(n):
    tong = 0
    while (n):
        tong = tong * 10 + n % 10
        n //= 10
    return tong


def ham6(n):
    dem = 0
    for i in range(2, isqrt(n) + 1):
        if (n % i == 0):
            dem += 1
            while (n % i == 0):
                n //= i
    if (n != 1):
        dem += 1
    return dem


def ham7(n):
    maxo = 0
    for i in range(2, isqrt(n)):
        if (n % i == 0):
            maxo = max(maxo, i)
            while (n % i == 0):
                n //= i
    if (n != 1):
        maxo = max(maxo, n)
    return maxo


def ham8(n):
    while (n):
        m = n % 10
        if (m == 6):
            return 1
        n //= 10
    return 0


def ham9(n):
    m = ham2(n)
    if (m % 8 == 0):
        return 1
    return 0


def ham10(n):
    tong = 0
    while (n):
        m = n % 10
        cnt = 1
        for i in range(1, m + 1):
            cnt *= i
        tong += cnt
        n //= 10
    return tong


def ham11(n):
    m = n % 10
    n //= 10
    while (n):
        k = n % 10
        if (m != k):
            return 0
        n //= 10
    return 1


def ham12(n):
    m = n % 10
    n //= 10
    while (n):
        k = n % 10
        if (k > m):
            return 0
        n //= 10
    return 1


def ham13(n):
    m = n
    dem = 0
    while (m):
        dem += 1
        m //= 10
    tong = 0
    while (n):
        k = n % 10
        tong += int(pow(k, dem))
        n //= 10
    return tong


if __name__ == '__main__':
    n = int(input())
    print(ham1(n))
    print(ham2(n))
    print(ham3(n))
    print(ham4(n))
    print(ham5(n))
    print(ham6(n))
    print(ham7(n))
    print(ham8(n))
    print(ham9(n))
    print(ham10(n))
    print(ham11(n))
    print(ham12(n))
    print(ham13(n))
