n = int(input())
tong = 0
for i in range(1, n + 1, 1):
    giaithua = 1
    for j in range(1, i + 1, 1):
        giaithua *= j
    tong += giaithua
print(tong)
