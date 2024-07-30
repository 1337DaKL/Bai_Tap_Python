from math import *


def uocchung(a, b):
    if b == 0:
        return a
    return uocchung(b, a % b)


def boicung(a, b):
    c = uocchung(a, b)
    return (a * b) // c


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(uocchung(a, b), boicung(a, b), sep=' ', end=' ')
