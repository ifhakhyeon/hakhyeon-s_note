import sys
input = sys.stdin.readline

R, C = map(int, input().split())
map = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    a = input()
    for j in range(C):
        if a[j] == '1':
            map[i][j] = 1
def check(y, x, type, time):
    if not 0 <= y <= C-1 or not 0 <= x <= R-1:
        return False
    if type == 0:
        target_y = y + time; target_x = x - time
        for _ in range(time):
            if 0 <= y+1 <= C-1 and 0 <= x-1 <= R-1 and map[y+1][x-1] == 1:
                y += 1; x -= 1
        if y == target_y and x == target_x:
            return True
        else:
            return False
    elif type == 1:
        target_y = y + time; target_x = x + time
        for _ in range(time):
            if 0 <= y+1 <= C - 1 and 0 <= x+1 <= R - 1 and map[y + 1][x + 1] == 1:
                y += 1; x += 1
        if y == target_y and x == target_x:
            return True
        else:
            return False
    elif type == 2:
        target_y = y - time; target_x = x + time
        for _ in range(time):
            if 0 <= y-1 <= C - 1 and 0 <= x+1 <= R - 1 and map[y - 1][x + 1] == 1:
                y -= 1; x += 1
        if y == target_y and x == target_x:
            return True
        else:
            return False
    elif type == 3:
        target_y = y - time; target_x = x - time
        for _ in range(time):
            if 0 <= y-1 <= C - 1 and 0 <= x-1 <= R - 1 and map[y - 1][x - 1] == 1:
                y -= 1; x -= 1
        if y == target_y and x == target_x:
            return True
        else:
            return False

def diamond(y, x, size):
    size -= 1
    if check(y, x, 0, size):
        y += size; x -= size
        if check(y, x, 1, size):
            y += size; x += size
            if check(y, x, 2, size):
                y -= size; x += size
                if check(y, x, 3, size):
                    return size+1
                return 0
            return 0
        return 0
    return 0

def solve(y, x, ret):
    if map[y][x] == 1:
        p = min((R-y+2)//2, C-x+1, x+1)
        for i in range(1, p+1):
            if p <= ret:
                break
            ret = max(ret, diamond(y, x, i))
        return ret
    else:
        return ret

ans = 0
for i in range(R):
    for j in range(C):
        ans = solve(i, j, ans)
print(ans)
