import sys
from collections import deque
input = sys.stdin.readline
Y, X = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(Y)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    ret = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dx[i]
            nx = x + dy[i]
            if 0 <= nx < X and 0 <= ny < Y and visited[ny][nx]==0:
                if area[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                elif area[ny][nx] == 1:
                    area[ny][nx] = 0
                    visited[ny][nx] = 1
                    ret += 1
    ans.append(ret)
    return ret

time = 0
while True:
    time += 1
    visited = [[0]*X for _ in range(Y)]
    ret = bfs()
    if ret == 0:
        break

print(time-1)
print(ans[-2])