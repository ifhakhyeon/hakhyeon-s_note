import sys

input = sys.stdin.readline
sdoku = []
f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
for _ in range(9):
    sdoku.append(list(map(int, f.readline().split())))
    # sdoku.append(list(map(int, input().split())))

def check1(y, n):
    for i in range(9):
        if n == sdoku[y][i]:
            return False
    return True

def check2(x, n):
    for i in range(9):
        if n == sdoku[i][x]:
            return False
    return True


def check3(y, x, n):
    part_y = (y // 3) * 3
    part_x = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if n == sdoku[part_y + i][part_x + j]:
                return False
    return True

zerolist = []
for y in range(9):
    for x in range(9):
        if sdoku[y][x] == 0:
            zerolist.append((y, x))

def dfs(idx):
    if idx == len(zerolist):
        for i in sdoku:
            for j in i:
                print(j, end=' ')
            print()
        exit(0)

    for i in range(1, 10):
        y = zerolist[idx][0]
        x = zerolist[idx][1]

        if check1(y, i) and check2(x, i) and check3(y, x, i):
            sdoku[y][x] = i
            dfs(idx+1)
            sdoku[y][x] = 0

if __name__ == "__main__":
    dfs(0)
