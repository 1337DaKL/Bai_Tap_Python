def chan(a, n):
    if (n == 0):
        if (a[n] % 2 == 0):
            return True
        else:
            return False
    else:
        if (a[n] % 2 == 1):
            return False
        else:
            return chan(a, n - 1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if (chan(a, n - 1)):
        print("YES")
    else:
        print("NO")
