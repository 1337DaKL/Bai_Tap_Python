n = int(input())
for i in range(1, n + 1, 1):
    for j in range(1, i + 1, 1):
        print('*', end='')
    print()
print()
for i in range(1, n + 1, 1):
    for j in range(1, n - i + 2, 1):
        print('*', end='')
    print()
print()
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if (i == n - j + 1):
            print('*', end='')
        elif (i > n - j + 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if (i == j):
            print('*', end='')
        elif (i > j):
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if (i == j or i == n or j == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
