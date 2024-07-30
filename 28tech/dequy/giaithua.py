def gaithua(n):
    if (n == 0):
        return 1
    return n * gaithua(n - 1)


if __name__ == '__main__':
    n = int(input())
    print(gaithua(n))
