import sys

# 재귀 깊이 때문에 런타임 에러 났었음..
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
C = int(input())
# RGB는 비용저장 [n번째 인덱스의][타입]
# 타입 0:빨, 1:초, 2:파
RGB = []
for _ in range(C):
    lgb = list(map(int, input().split()))
    RGB.append(lgb)
# RGB = [[?,?,?],[?,?,?],[?,?,?]...] 의 형태
cache = [[-1, -1, -1] for _ in range(C + 10)]


def paint(N, type):
    # 기저 사례
    if N == C:
        return 0

    if cache[N][type] != -1:
        return cache[N][type]
    # 자기 자신을 칠하는데 드는 비용
    cache[N][type] = RGB[N][type]

    # 지금 타입에 따라 다음 색을 결정한다.
    if type == 0:
        plus = min(paint(N + 1, 1), paint(N + 1, 2))
        cache[N][type] += plus

    elif type == 1:
        plus = min(paint(N + 1, 0), paint(N + 1, 2))
        cache[N][type] += plus

    elif type == 2:
        plus = min(paint(N + 1, 0), paint(N + 1, 1))
        cache[N][type] += plus

    return cache[N][type]


ret = 9876543210
for i in range(3):
    ret = min(ret, paint(0, i))

print(ret)