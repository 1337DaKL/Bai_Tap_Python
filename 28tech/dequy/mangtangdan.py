    def tangdan(a, n):
        if (n == 1):
            if (a[0] < a[1]):
                return True
            else:
                return False
        else:
            if (a[n - 1] >= a[n]):
                return False
            else:
                return tangdan(a, n - 1)


    if __name__ == '__main__':
        n = int(input())
        a = list(map(int, input().split()))
        if (tangdan(a, n - 1)):
            print("YES")
        else:
            print("NO")
