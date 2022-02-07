cache = [[0 for _ in range(100)] for _ in range(100)]

triangle = [[0 for _ in range(100)] for _ in range(100)]

n = 100

def path(y, x):
    if y == n-1:
        return triangle[y][x]
    if cache[y][x] != -1:
        return cache[y][x]
    cache[y][x] = max(path(y+1, x), path(y+1, x+1)) + triangle[y][x]
    return cache[y][x]