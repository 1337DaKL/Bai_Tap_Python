n = int(input())
a = list(map(int, input().split()))
m = int(input())
dem = 0
for i in range(0, len(a), 1):
    for j in range(i + 1, len(a), 1):
        if a[i] + a[j] == m:
            dem += 1
print(dem)
