n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        a[i] = a[i]
    else:
        a[i] = a[i] + a[i - 1]
for i in a:
    print(i, end=' ')
