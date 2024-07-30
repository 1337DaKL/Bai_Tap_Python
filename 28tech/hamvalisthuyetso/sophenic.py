import math
from decimal import Decimal


def phenic(n):
    dem = 0
    dem2 = 0
    for i in range(2, int(n.sqrt()) + 1, 1):
        if (n % i == 0):
            dem += 1
            while n % i == 0:
                dem2 += 1
                n /= i
    if dem == 3 and dem2 == 3:
        return True
    else:
        return False


if __name__ == '__main__':
    n = Decimal(input())
    if phenic(n):
        print(1)
    else:
        print(0)
z``