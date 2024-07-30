from math import *


def kiemtranguyento(n):
    for i in range(2, isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return n > 1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, n, 1):
        tongtrai, tongphai = 0, 0
        if i == 0:
            for j in range(i + 1, n, 1):
                tongphai += a[j]
        elif i == 0:
            for j in range(0, i, 1):
                tongtrai += a[j]
        else:
            for j in range(i + 1, n, 1):
                tongphai += a[j]
            for j in range(0, i, 1):
                tongtrai += a[j]
        if kiemtranguyento(tongphai) and kiemtranguyento(tongtrai):
            print(i, end=' ')
