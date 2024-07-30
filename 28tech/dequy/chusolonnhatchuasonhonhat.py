def lonnhat(n):
    if (n == 0):
        return 0
    return max(n % 10, lonnhat(n // 10))


def nhonhat(n):
    if (n // 10 == 0):
        return n
    return min(n % 10, nhonhat(n // 10))


if __name__ == '__main__':
    n = int(input())
    print(lonnhat(n), nhonhat(n), sep=' ')
