import sys
input = sys.stdin.readline
# key = lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)
# list = list(map(int, f.readline().split()))

INF = 9876543210
# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# n, m = map(int, f.readline().split())
n, m = map(int, input().split())
dist = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    # y, x, c = map(int, f.readline().split())
    y, x, c = map(int, input().split())
    dist[y-1][x-1] = c

cache = [[-1 for _ in range((1 << (n+1)))] for _ in range(n+1)]

def dp(here, visited, cost):
    if visited == (1 << n)-1:
        return dist[here][0] or INF

    if cache[here][visited] > 0:
        return cache[here][visited]

    ret = INF

    for next in range(n):
        # n번째 수가 있나 없나 확인 할 때 (0이면 없고, 1 이상이면 있는 것)
        # print(bin(0b *1* 010 & (1 << 3)))  #  0b *1* 000
        if dist[here][next] == 0 or (visited & (1 << next)) != 0:
            continue
        ret = min(ret, dp(next, (1 << next) | visited))

    cache[here][visited] = ret
    return ret

maxcost = dp(0, 1 << 0)
for i in dist:
    print(i)

for i in cache:
    print(i)

ans = [0 for _ in range(n)]

def dfs(idx, here, visited):
    if idx == n and dist[here][0] <= maxcost:
        for i in ans:
            print(i+1, end=' ')
        exit(0)

    for next in range(n):
        if 0 < dist[here][next] <= maxcost and (visited & (1 << next)) == 0:
            ans[idx] = next
            dfs(idx + 1, next, (1 << next) | visited)
            ans[idx] = -1

if maxcost > 0:
    print(maxcost)
    dfs(1, 0, 1 << 0)
else:
    print(-1)
