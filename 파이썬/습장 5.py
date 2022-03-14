import sys
input = sys.stdin.readline
C = int(input())
for _ in range(C):
    stone = list(map(int, input().split()))
    a = sum(stone)
    if 1 not in stone:
        if a % 2 == 0:
            if a % 4 == 0:
                print('R')
            else:
                print('B'
                      '')
        else:
            if a % 4 == 3:
                print('B')
            else:
                print('R')
    else:
        stone.sort()
        if stone[1] % 2 == 1 and stone[1] == stone[2]:
            print('B')
        else:
            print('R')