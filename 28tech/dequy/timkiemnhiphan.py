from math import *


def binary(a, l, r, x):
    if (l > r):
        return False
    mid = (l + r) // 2
    if (a[mid] == x):
        return True
    elif (a[mid] < x):
        return binary(a, mid + 1, r, x)
    else:
        return binary(a,  l, mid - 1,  x)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = int(input())
    if (binary(a, 0, n - 1,  x)):
        print(1)
    else:
        print(0)
