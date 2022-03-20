import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
where = [0 for _ in range(100000+1)]
go = deque()
go.append(N)

while where[K] == 0:
    now = go.popleft()
    if now == K:
        break
    if 100000 >= now + 1 >= 0 and not where[now + 1]:
        where[now + 1] = where[now] + 1
        go.append(now + 1)
    if 100000 >= now - 1 >= 0 and not where[now - 1]:
        where[now - 1] = where[now] + 1
        go.append(now - 1)
    if now != 0 and 100000 >= 2*now > 0 and not where[2 * now]:
        where[2 * now] = where[now] + 1
        go.append(2*now)

print(where[K])

import sys
from collections import deque
input = sys.stdin.readline()
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[x] +1
                q.append(j)
MAX = 100000
n,k = map(int,input.split())
dist = [0] * (MAX+1)
bfs()
