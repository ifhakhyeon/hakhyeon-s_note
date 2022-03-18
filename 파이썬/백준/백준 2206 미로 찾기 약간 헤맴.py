import sys
from collections import deque
input = sys.stdin.readline

Y, X = map(int, input().split())
maze = []
for _ in range(Y):
    maze.append(list(map(int, input().strip())))

cache = [[[0, 0] for _ in range(X)] for _ in range(Y)]
cache[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(y, x):
    go = deque()
    go.append((y, x, 0))
    while go:
        y, x, b = go.popleft()
        if y == Y-1 and x == X-1:
            return cache[y][x][b]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= Y or nx < 0 or nx >= X:
                continue

            elif maze[ny][nx] == 0 and cache[ny][nx][b] == 0:
                cache[ny][nx][b] = cache[y][x][b] + 1
                go.append((ny, nx, b))

            elif maze[ny][nx] == 1 and b == 0:
                cache[ny][nx][1] = cache[y][x][b] + 1
                go.append((ny, nx, 1))

    return -1

print(bfs(0, 0))