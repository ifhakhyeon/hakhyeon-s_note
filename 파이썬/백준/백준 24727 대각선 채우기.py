import sys
input = sys.stdin.readline

N = int(input())
area = [[0]*N for _ in range(N)]
C, E = map(int, input().split())
e_s = [0, 0]
c_s = [N-1, N-1]
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

def check(y, x):
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if area[ny][nx] != 0 and area[ny][nx] != area[y][x]:
                return False
    return True

ans = True

for i in range(E):
    area[e_s[0]][e_s[1]] = 2
    if 0 <= e_s[0] - 1 < N and 0 <= e_s[1] + 1 < N:
        e_s[0] -= 1
        e_s[1] += 1
    else:
        s = sum(e_s)
        e_s[0] = min(s+1, N-1)
        e_s[1] = max(0, s-N+2)

for i in range(C):
    area[c_s[0]][c_s[1]] = 1
    if not check(c_s[0], c_s[1]):
        ans = False
        break
    if 0 <= c_s[0] + 1 < N and 0 <= c_s[1] - 1 < N:
        c_s[0] += 1
        c_s[1] -= 1
    else:
        s = sum(c_s)
        c_s[0] = max(s - N, 0)
        c_s[1] = s - c_s[0] - 1

if ans:
    print(1)
    for i in area:
        for j in i:
            print(j,end='')
        print()
else:
    print(-1)
