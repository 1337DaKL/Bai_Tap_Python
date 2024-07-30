from math import *


def songuyentolonnhat(n):
    maxo = 0
    for i in range(2, int(isqrt(n)) + 1, 1):
        if (n % i == 0):
            maxo = max(maxo, i)
            while (n % i == 0):
                n //= i
    if n > 1:
        maxo = max(maxo, n)
    return maxo


if __name__ == '__main__':
    test = int(input())
    while (test):
        test -= 1
        n = int(input())
        print(songuyentolonnhat(n), end='\n')
