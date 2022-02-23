import sys
def rl():
    return sys.stdin.readline()
def solution(Russia, Korea):
    Russia.sort()
    Korea.sort()
    win = 0
    for Ru in Russia:
        for i, Ko in enumerate(Korea):
            if Ru <= Ko:
                win += 1
                Korea.pop(i)
                break
    return win

for case in range(int(rl())):
    teamCount = int(rl())
    Russia = list(map(int, rl().split()))
    Korea = list(map(int, rl().split()))
    print(solution(Russia, Korea))

