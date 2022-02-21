import sys
input = sys.stdin.readline

n = int(input())
cache = [[-1 for _ in range(n)] for _ in range(n)]
triangle = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    triangle[i][0:i+1] = list(map(int, input().split()))

def path(y, x):
    if y == n-1:
        return triangle[y][x]
    if cache[y][x] != -1:
        return cache[y][x]
    cache[y][x] = max(path(y+1, x), path(y+1, x+1)) + triangle[y][x]

    return cache[y][x]

print(path(0, 0))