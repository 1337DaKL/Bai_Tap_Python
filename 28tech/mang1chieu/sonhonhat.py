n = int(input())
a = list(map(int, input().split()))
c = min(a)
dem = 0
for i in range(0, len(a), 1):
    if a[i] == c:
        dem += 1
print(dem)
