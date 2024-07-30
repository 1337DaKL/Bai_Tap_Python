def chan(n):
    if (n < 10):
        if (n % 2 == 0):
            return n
        else:
            return 0
    m = n % 10
    if (m % 2 == 0):
        return m + chan(n // 10)
    else:
        return chan(n // 10)


def le(n):
    if (n < 10):
        if (n % 2 == 1):
            return n
        else:
            return 0
    m = n % 10
    if (m % 2 == 1):
        return m + le(n // 10)
    else:
        return le(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(chan(n))
    print(le(n))
