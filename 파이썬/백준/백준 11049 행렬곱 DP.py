import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
cache = [[0 for i in range(n)] for i in range(n)]
INF = 9876543210
# 인접한 2개의 행렬은 미리 곱하여 배열에 넣는다.
for i in range(n - 1):
    cache[i][i + 1] = matrix[i][0] * matrix[i + 1][0] * matrix[i + 1][1]


def peek(start, end):
    if cache[start][end] != 0:
        return cache[start][end]

    if start == end:
        return 0

    ret = INF
    for i in range(start, end):
        temp = peek(start, i) + peek(i + 1, end) + matrix[start][0] * matrix[i + 1][0] * matrix[end][1]
        ret = min(ret, temp)
    cache[start][end] = ret
    return ret


print(peek(0, n - 1))

