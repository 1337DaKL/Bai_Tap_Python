n = int(input())
a = list(map(int,  input().split()))
ok = True
for i in range(0, len(a), 2):
    if a[i] % 2 == 0:
        print(a[i], end=' ')
        ok = False
if ok:
    print("NONE")
