import sys
input = sys.stdin.readline

C = int(input())
for i in range(C):
    n = int(input())
    f = list(map(int, input().split()))
    cache = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1):
        # 대각 채우기
        cache[i][i + 1] = f[i] + f[i + 1]
        for j in range(i + 2, n):
            # 합의 누적 처리하기
            cache[i][j] = cache[i][j - 1] + f[j]

    for s in range(2, n):
        for i in range(n - s):
            j = i + s
            # 크누스 최적화..
            cache[i][j] += min([cache[i][k] + cache[k + 1][j] for k in range(i, j)])

    print(cache[0][n - 1])