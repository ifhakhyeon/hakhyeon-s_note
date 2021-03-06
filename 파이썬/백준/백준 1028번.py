import sys
input = sys.stdin.readline

R, C = map(int, input().split())

map = [input().strip() for _ in range(R)]

cache = [[[-1, -1, -1, -1] for _ in range(C)] for _ in range(R)]

def check(y, x, type, maxsize):
    if not 0 <= y <= R-1 or not 0 <= x <= C-1:
        return 0
    if type == 0 and 0 <= y+1 <= R-1 and 0 <= x-1 <= C-1:
        if cache[y][x][type] != -1:
            return cache[y][x][type]
        if map[y+1][x-1] == '1':
            cache[y][x][type] = 1 + check(y+1, x-1, 0, maxsize)
            if cache[y][x][type] > maxsize:
                return maxsize
            return cache[y][x][type]
        elif map[y+1][x-1] == '0':
            cache[y][x][type] = 0
            return cache[y][x][type]

    elif type == 1 and 0 <= y+1 <= R-1 and 0 <= x+1 <= C-1:
        if cache[y][x][type] != -1:
            return cache[y][x][type]
        if map[y+1][x+1] == '1':
            cache[y][x][type] = 1 + check(y+1, x+1, 1, maxsize)
            if cache[y][x][type] > maxsize:
                return maxsize
            return cache[y][x][type]
        elif map[y+1][x+1] == '0':
            cache[y][x][type] = 0
            return cache[y][x][type]

    elif type == 2 and 0 <= y-1 <= R-1 and 0 <= x+1 <= C-1:
        if cache[y][x][type] != -1:
            return cache[y][x][type]
        if map[y-1][x+1] == '1':
            cache[y][x][type] = 1 + check(y-1, x+1, 2, maxsize)
            if cache[y][x][type] > maxsize:
                return maxsize
            return cache[y][x][type]
        elif map[y-1][x+1] == '0':
            cache[y][x][type] = 0
            return cache[y][x][type]

    elif type == 3 and 0 <= y-1 <= R-1 and 0 <= x-1 <= C-1:
        if cache[y][x][type] != -1:
            return cache[y][x][type]
        if map[y-1][x-1] == '1':
            cache[y][x][type] = 1 + check(y-1, x-1, 3, maxsize)
            if cache[y][x][type] > maxsize:
                return maxsize
            return cache[y][x][type]
        elif map[y-1][x-1] == '0':
            cache[y][x][type] = 0
            return cache[y][x][type]
    else:
        return 0
# ?????? ???????????? ??????????????? ???????????? ???????????? ??????.
def diamond(y, x, size, maxsize):
    if 0 <= y+1 <= R-1 and 0 <= x+1 <= C-1 and map[y+1][x+1] == '0':
        return -1
    # 1??? ?????? ????????? ???????????? n????????? ??????????????? ??????????????? Y-1?????? ???????????? ??????
    size -= 1
    up = check(y, x, 0, maxsize)
    left = check(y+size, x-size, 1, maxsize)
    down = check(y+size*2, x, 2, maxsize)
    right = check(y+size, x+size, 3, maxsize)
    if up >= size and left >= size and down >= size and right >= size:
        return size+1
    else:
        return -1

def solve(y, x, ret, maxsize):
    if map[y][x] == '1':
        # p??? Y,x?????? ????????? ?????????????????? ??????
        p = min((R-y+2)//2, C-x+1, x+1)
        # ????????? ????????? ?????? ???????????? ???????????? ??????
        if p > ret:
            # p?????? ???????????? p ?????? ??????
            for i in reversed(range(ret, p+1)):
                can = diamond(y, x, i, maxsize)
                # ??? ??? ???????????? ???????????? ?????? ??? ?????? ret?????? ????????? ?????? x
                if ret < can:
                    return can
            return ret
        return ret
    else:
        return ret

ans = 0
maxsize = (min(R, C)+1)//2
for i in range(R):
    for j in range(C):
        ans = solve(i, j, ans, maxsize)
        if ans == maxsize:
            break
    if ans == (min(R, C) + 1) // 2:
        break

print(ans)
