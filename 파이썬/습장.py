import sys
input = sys.stdin.readline

R, C = map(int, input().split())
map = [[0 for _ in range(C)] for _ in range(R)]
#           ↙   ↘   ↗   ↖
cache = [[[0, 0, 0, 0] for _ in range(C)] for _ in range(R)]
for i in range(R):
    a = input()
    for j in range(C):
        if a[j] == '1':
            map[i][j] = 1
def check(y, x, type):
    if type == 0:
        if 0 <= y <= C-1 and 0 <= x <= R-1 and map[y+1][x-1] == 1:
            # cache[y][x][type] = 1
            return True
        return False
    if type == 1:
        if 0 <= y <= C-1 and 0 <= x <= R-1 and map[y+1][x+1] == 1:
            # cache[y][x][type] = 1
            return True
        return False
    if type == 2:
        if 0 <= y <= C-1 and 0 <= x <= R-1 and map[y-1][x+1] == 1:
            # cache[y][x][type] = 1
            return True
        return False
    if type == 3:
        if 0 <= y <= C-1 and 0 <= x <= R-1 and map[y-1][x-1] == 1:
            # cache[y][x][type] = 1
            return True
        return False

def solve(y, x):
    if not 0 <= y <= C-1 or not 0 <= x <= R-1:
        return False
    ret = 0
    if map[y][x] == 1:
        type = 0
        while check(y, x, type):
            y += 1
            x -= 1
            ret += 1
        type += 1
        if ret != 0:
            while check(y, x, type):
                y += 1
                x += 1
            type += 1
            while check(y, x, type):
                y -= 1
                x += 1
            type += 1
            while check(y, x, type):
                y -= 1
                x -= 1
