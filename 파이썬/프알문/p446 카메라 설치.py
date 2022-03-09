import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# C = int(f.readline())
C = int(input())

def decision(location, cameras, gap):
    limit = -1
    installed = 0
    for i in range(len(location)):
        if limit <= location[i]:
            installed += 1
            limit = location[i] + gap

    return installed >= cameras

def optimize(location, cameras):
    lo = 0
    hi = 241
    for it in range(100):
        mid = (lo + hi) / 2.0
        if decision(location, cameras, mid):
            lo = mid
        else:
            hi = mid
    return lo

for _ in range(C):
    # N, M = map(float, f.readline().split())
    N, M = map(float, input().split())
    # location = list(map(float, f.readline().split()))
    location = list(map(float, input().split()))

    a = optimize(location, N)
    if (100 * a) - int(100 * a) >= 5:
        a += 0.01
    print(f'{a:.2f}')
exit(0)