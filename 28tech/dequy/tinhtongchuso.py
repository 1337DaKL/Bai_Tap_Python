def tong(n):
    if (n == 0):
        return 0
    return n % 10 + tong(n // 10)


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        print(1)
    print(tong(n))
