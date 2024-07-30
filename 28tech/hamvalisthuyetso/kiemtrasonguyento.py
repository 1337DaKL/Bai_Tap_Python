import math


def songuyento(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if (n % i == 0):
            return False
    return n > 1


if __name__ == '__main__':
    n = int(input())
    if (songuyento(n)):
        print("YES")
    else:
        print("NO")
