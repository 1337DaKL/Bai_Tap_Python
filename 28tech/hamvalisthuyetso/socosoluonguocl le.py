from math import *

if __name__ == '__main__':
    n = int(input())
    nn = int(isqrt(n))
    if (nn * nn == n):
        print("YES")
    else:
        print("NO")
