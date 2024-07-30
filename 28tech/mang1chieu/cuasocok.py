n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, n - m + 1, 1):
    tong = 0
    for j in range(i, i + m):
        tong += a[j]
    print(tong, end=' ')
