def nhiphan(n):
    if (n == 1):
        return '1'
    return nhiphan(n // 2) + str(n % 2)


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        print(0)
    else:
        print(nhiphan(n))
