buttonlist = [[0, 1, 2, -1, -1],
              [3, 7, 9, 11, -1],
              [4, 10, 14, 15, -1],
              [0, 4, 5, 6, 7],
              [6, 7, 8, 10, 12],
              [0, 2, 14, 15, -1],
              [3, 14, 15, -1, -1],
              [4, 5, 7, 14, 15],
              [1, 2, 3, 4, 5],
              [3, 4, 5, 9, 13]]

clock = [12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6]
# clock = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

# 버튼을 누르면 시계가 바뀌는 함수
def pressbutton(button, clock):
    for i in buttonlist[button]:
        if i == -1:
            break
        else:
            clock[i] += 3
            if clock[i] == 15:
                clock[i] =3

def press(N, pressed):
    pressed.apend(N)

def checkans(clock):
    ok = True
    for i in clock:
        if i != 12:
            ok = False
            break
    return ok

INF = 9999

def solve(button, clock):

    if button == 10:
        if checkans(clock):
            # print("성공")
            return 0
        else:
            return INF

    ret = INF

    for i in range(4):
        ret = list(min(ret, i+solve(button+1, clock)))
        pressbutton(button, clock)

    return ret


print(solve(0,clock))