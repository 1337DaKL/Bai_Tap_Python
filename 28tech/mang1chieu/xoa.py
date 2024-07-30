n, m = map(int, input().split())
a = list(map(int, input().split()))
if m not in a:
    print("NOT FOUND")
else:
    for i in range(n):
        if a[i] == m:
            a.pop(i)
            break
    for i in range(n - 1):
        print(a[i], end=' ')
