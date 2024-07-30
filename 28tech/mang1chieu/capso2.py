n = int(input())
a = list(map(int, input().split()))
a.sort()
mino = 100000
for i in range(1, len(a), 1):
    if a[i] - a[i - 1] < mino:
        mino = a[i] - a[i - 1]
print(mino)
