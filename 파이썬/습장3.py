import math
import sys
from math import sqrt
input = sys.stdin.readline

E = int(input())

Vroot = [i for i in range(E + 1)]
Elist = []
star = [list(map(float, input().split()))]
n = 2

def cal(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


for _ in range(E-1):
    k = list(map(float, input().split()))
    for i in range(1, n):
        Elist.append([i, n, cal(star[i-1], k)])
    star.append(k)
    n += 1


Elist.sort(key=lambda x: x[2])


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)

    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w

print(answer)