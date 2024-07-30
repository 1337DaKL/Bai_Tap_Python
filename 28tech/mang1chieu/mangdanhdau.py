n = int(input())
a = list(map(int, input().split()))
b = []
dem = 0
for i in range(0, n, 1):
    if a[i] not in b:
        dem += 1
        b.append(a[i])
print(dem)
