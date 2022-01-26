import sys

input = sys.stdin.readline

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


def pressbutton(button, clock):
    for i in buttonlist[button]:
        if i == -1:
            break
        else:
            clock[i] += 3
            if clock[i] == 15:
                clock[i] = 3


def checkans(clock):
    ok = True
    for i in clock:
        if i != 12:
            ok = False
            break
    return ok

def solve(clock):
    ret = 0
    for _ in range((12-clock[13])//3):
        pressbutton(9, clock)
        ret += 1

    for _ in range((12-clock[9])//3):
        pressbutton(1, clock)
        ret += 1

    for _ in range((12-clock[12])//3):
        pressbutton(4, clock)
        ret += 1

    for _ in range((12-clock[10])//3):
        pressbutton(2, clock)
        ret += 1

    for _ in range((12-clock[6])//3):
        pressbutton(3, clock)
        ret += 1

    for _ in range((12-clock[7])//3):
        pressbutton(7, clock)
        ret += 1

    for _ in range((12-clock[5])//3):
        pressbutton(8, clock)
        ret += 1

    for _ in range((12-clock[3])//3):
        pressbutton(6, clock)
        ret += 1

    for _ in range((12-clock[14])//3):
        pressbutton(5, clock)
        ret += 1

    for _ in range((12 - clock[0]) // 3):
        pressbutton(0, clock)
        ret += 1

    if checkans(clock):
        return ret
    else:
        return -1

C = int(input())

for _ in range(C):
    clock = list(map(int, input().split()))
    if clock[14] != clock[15]:
        print(-1)
    elif clock[8] != clock[12]:
        print(-1)
    else:
        print(solve(clock))

# 알게 된것 파이썬은 런타임이 길구나..
# 조학현 넌 수학과야!