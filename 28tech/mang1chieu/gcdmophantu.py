def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ok = gcd(a[1], a[0])
    for i in range(2, n):
        ok = gcd(ok, a[i])
    print(ok)
