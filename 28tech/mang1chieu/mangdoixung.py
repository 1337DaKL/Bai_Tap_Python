def doixung(a, n):
    for i in range(0, n // 2, 1):
        if a[i] != a[n - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if doixung(a, n):
        print('YES')
    else:
        print('NO')
