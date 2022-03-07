import sys
input = sys.stdin.readline
# key=lambda x: x[1]
# sys.setrecursionlimit(10 ** 6)
# list = list(map(int, f.readline().split()))

# f = open(r"C:\Users\H30208\Desktop\조학현 공부노트\input.txt", 'r')
# X, Y = map(int, f.readline().split())
X, Y = map(int, input().split())
tomato = []
go_y = [1, -1, 0, 0]
go_x = [0, 0, 1, -1]

def where(tomato_field):
    where_tomato = []
    for y in range(Y):
        for x in range(X):
            if tomato_field[y][x] == 1:
                where_tomato.append((y, x))
    return where_tomato

def day(where_tomato):
    next_day = []
    for mato in where_tomato:
        for i in range(4):
            if 0 <= mato[0] + go_y[i] < Y \
                    and 0 <= mato[1] + go_x[i] < X \
                    and not tomato[mato[0]+go_y[i]][mato[1]+go_x[i]]:
                tomato[mato[0]+go_y[i]][mato[1]+go_x[i]] = 1
                next_day.append((mato[0]+go_y[i], mato[1]+go_x[i]))
    return next_day

for _ in range(Y):
    # tomato.append(list(map(int, f.readline().split())))
    tomato.append(list(map(int, input().split())))

next_tomato = where(tomato)
tomato_time = 0
while True:
    next_tomato = day(next_tomato)
    if next_tomato:
       tomato_time += 1
    else:
        break

full_tomato = True

for i in tomato:
    if 0 in i:
        full_tomato = False

if full_tomato:
    print(tomato_time)
else:
    print(-1)