import sys
input = sys.stdin.readline
C = int(input())

for _ in range(C):
    stone = list(map(int, input().split()))
    stone.sort()
    if stone[0] % 2 == 1:
        if (stone[0] // 2) % 2 == 0:
            if stone[1] == stone[2] and stone[1] % 2 == 1:
                print('B')
            else:
                print('R')
        else:
            if stone[1] == stone[2] and stone[1] % 2 == 0:
                print('B')
            else:
                print('R')
    else:
        if stone[1] % 2 == 0:
            print('B')
        else:
            print('R')