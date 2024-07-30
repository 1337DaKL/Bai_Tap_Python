from math import *
n, m = map(int, input().split())
nn = int(isqrt(n))
if (nn * nn != n):
    nn += 1
print(int(isqrt(m)) + 1 - nn + 1)
