fi = [0, 1]


def fibo():
    for i in range(2, 100):
        tong = fi[i - 1] + fi[i - 2]
        fi.append(tong)


if __name__ == '__main__':
    fibo()
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] in fi:
            print(a[i], end=' ')
