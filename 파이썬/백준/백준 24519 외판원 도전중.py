import sys
import math
input = sys.stdin.readline


INF = math.inf
n, m = map(int, input().split())
dist = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y, x, c = map(int, input().split())
    dist[y-1][x-1] = c

cache = [[-1 for _ in range((1 << (n+1)))] for _ in range(n+1)]


def dp(here, visited, m_cost):
    if visited == (1 << n) - 1:
        return max(m_cost, dist[here][0]) if dist[here][0] != 0 else INF

    if cache[here][visited] != -1 and cache[here][visited] <= m_cost:
        return m_cost

    ret = INF

    for next in range(n):
        if dist[here][next] == 0 or visited & (1 << next) != 0:
            continue
        ret = min(ret, dp(next, (1 << next) | visited, max(m_cost, dist[here][next])))

    cache[here][visited] = max(ret, cache[here][visited])
    return ret

# print(bin((1 << 0)|(1<<2)|(1<<3)|(1<<4)|(1<<5)))
maxcost = dp(2, (1 << 0)|(1<<2), -INF)

# for i in dist:
#     print(i)

# for i in cache:
#     for j in enumerate(i):
#         if j[1] != -1:
#             print(bin(j[0]), j[1], end=' ')
#     print()

ans = [0 for _ in range(n)]


def dfs(idx, here, visited):
    if visited == (1 << n) - 1 and dist[here][0] <= maxcost:
        for i in ans:
            print(i+1, end=' ')
        exit(0)

    for next in range(n):
        if 0 < dist[here][next] <= maxcost and (visited & (1 << next)) == 0:
            ans[idx] = next
            dfs(idx + 1, next, (1 << next) | visited)


if maxcost > 0 and maxcost != INF:
    print(maxcost)
    dfs(1, 0, 1 << 0)
else:
    print(-1)
