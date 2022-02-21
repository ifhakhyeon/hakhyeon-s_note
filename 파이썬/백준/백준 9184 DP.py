import sys
input = sys.stdin.readline

cache = [[[-987645321 for _ in range(102)] for _ in range(102)] for _ in range(102)]

def w(a, b, c):
    if cache[a][b][c] != -987645321:
        return cache[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        cache[a][b][c] = 1
        return cache[a][b][c]

    elif a > 20 or b > 20 or c > 20:
        cache[a][b][c] = w(20, 20, 20)

    elif a < b and b < c:
        cache[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) -w(a, b-1, c)

    else:
        cache[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return cache[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) =', w(a, b, c))