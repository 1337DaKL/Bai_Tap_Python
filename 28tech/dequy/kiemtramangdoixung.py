def dx9(a, l, r):
    if (l == r):
        return True
    else:
        if (a[l] == a[r]):
            return dx9(a, l + 1, r - 1)
        else:
            return False


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if (dx9(a, 0, n - 1)):
        print("YES")
    else:
        print("NO")
