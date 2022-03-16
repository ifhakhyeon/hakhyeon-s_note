import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()

def check(house, dist):
    wifi = C - 1
    start = 0
    for i in range(start + 1, N):
        if house[i] - house[start] >= dist:
            start = i
            wifi -= 1
            if wifi == 0:
                break
    return True if wifi == 0 else False

def place(start, end):
    if start == end:
        return start
    if start+1 == end:
        return end if check(house, end) else start
    mid = (start + end)//2
    if check(house, mid):
        return place(mid, end)
    else:
        return place(start, mid)

print(place(0, house[-1] - house[0]))