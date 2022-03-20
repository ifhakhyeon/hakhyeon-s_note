import sys
from collections import deque
input = sys.stdin.readline
import math

C = int(input())

def bfs():
    go = deque()
    go.append(start)
    while go:
        y, x = go.popleft()
        if y == end[0] and x == end[1]:
            return chess[end[0]][end[1]]
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not chess[ny][nx]:
                chess[ny][nx] = chess[y][x] + 1
                go.append([ny, nx])

for _ in range(C):
    a = math.inf
    N = int(input())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    chess = [[0] * N for _ in range(N)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs())