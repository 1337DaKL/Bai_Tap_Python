a, b, c, d, e = map(int, input().split())
tong = a + b + c + d + e
if (tong % 5 == 0 and tong // 5 != 0):
    print(tong // 5)
else:
    print(-1)
