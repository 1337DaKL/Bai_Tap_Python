def fist(n):
    if n // 10 == 0:
        return n
    return fist(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(fist(n))
