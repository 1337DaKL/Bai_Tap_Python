n = int(input())
tong = 0.0
for i in range(0, n, 1):
    cnt = 1
    if (i == 0):
        tong += 1
    else:
        for j in range(1, i + 1, 1):
            cnt *= j
        tong += (1 / cnt)
print('%.4f' % tong)
