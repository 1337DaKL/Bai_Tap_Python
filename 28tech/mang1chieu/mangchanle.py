from math import *
from sys import stdin
if __name__ == '__main__':
    a = []
    for s in stdin:
        a += list(map(int, s.split()))
    chan, le = 0, 0
    for i in a:
        if (i % 2 == 0):
            chan += 1
        else:
            le += 1
    if chan > le:
        print("CHAN")
    elif le > chan:
        print("LE")
    else:
        print("CHANLE")
