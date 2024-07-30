n = int(input())
a = list(map(int, input().split()))
mino = min(a)
maxo = max(a)
for i in range(n - 1, -1, - 1):
    if mino == a[i]:
        print(i, end=' ')
        break
for i in range(n):
    if maxo == a[i]:
        print(i)
        break
