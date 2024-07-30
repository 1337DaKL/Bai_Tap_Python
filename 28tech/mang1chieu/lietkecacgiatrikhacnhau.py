
if __name__ == '__main__':
    n = int(input())
    a = list()
    b = list(map(int, input().split()))
    for i in range(0, n, 1):
        if b[i] not in a:
            a.append(b[i])
            print(b[i], end=' ')
