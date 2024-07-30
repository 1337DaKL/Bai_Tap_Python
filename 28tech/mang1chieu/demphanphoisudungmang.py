n = int(input())
a = list(map(int, input().split()))
check = list()
for i in range(n):
    if a[i] not in check:
        print(a[i], a.count(a[i]), sep=' ', end='\n')
        check.append(a[i])
print()
a.sort()
mino, maxo = 1001, 0
ok = list()
for i in range(n):
    if a[i] not in ok:
        print(a[i], a.count(a[i]), sep=' ', end='\n')
        ok.append(a[i])
        mino = min(mino, a.count(a[i]))
        maxo = max(maxo, a.count(a[i]))
print()
for i in range(n - 1, -1, -1):
    if a.count(a[i]) == maxo:
        print(a[i], end='\n')
        break
for i in range(n):
    if a.count(a[i]) == mino:
        print(a[i])
        break
