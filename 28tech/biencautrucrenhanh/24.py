if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n, m, u = map(int, input().split())
        a = [set for _ in range(n)]
        for _ in range(m):
            x, y = map(int, input().split())
