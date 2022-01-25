button = [[0, 1, 2, -1, -1],
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

# N번째 버튼을 누르면 시계가 바뀌는 함수
def pressbutton(N, clock):
    for i in button[N]:
        if i == -1:
            break
        clock[i] += 3

        if clock[i] >12:
            clock[i] %= 12
    return clock

def press(N, pressed):
    pressed.apend(N)
def checkans(clock):
    ok = True
    for i in clock:
        if i != 12:
            ok = False
            break
    return ok

def slove(N, clock, pressed):

    if checkans(clock):
        return pressed

    for i in range(10):
        for j in range(4):
            press(N,)
            pressbutton(i,clock,)


# print(checkans(clock))