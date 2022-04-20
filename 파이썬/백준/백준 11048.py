import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

Y, X = map(int, input().split())
area = []
for _ in range(Y):
    area.append(list(map(int, input().split())))
dy = [0, 1, 1]
dx = [1, 0, 1]

cache = [[-1] * X for _ in range(Y)]

def candy(y, x):
    if cache[y][x] != -1:
        return cache[y][x]
    if y == Y-1 and x == X-1:
        return area[y][x]
    ret = 0
    for d in range(3):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < Y and 0 <= nx < X:
            ret = max(ret, candy(ny, nx) + area[y][x])
    cache[y][x] = ret
    return ret

print(candy(0, 0))

Y, X = map(int, input().split())
area = []
for _ in range(Y):
    area.append(list(map(int, input().split())))
cache = [[0] * (X+1) for _ in range(Y+1)]
for i in range(1, Y+1):
    for j in range(1, X+1):
        cache[i][j] = area[i-1][j-1] + max(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])
print(cache[Y][X])