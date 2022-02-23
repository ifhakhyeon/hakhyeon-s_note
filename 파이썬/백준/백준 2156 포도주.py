import sys
input = sys.stdin.readline
n = int(input())
# 재귀 깊이 런타임 애러 생각하기
sys.setrecursionlimit(10 ** 5)

cache = [[-1 for _ in range(n + 1)] for _ in range(4)]


grape = [0]
for _ in range(n):
    grape.append(int(input()))

def drink(can, idx):
    # 기저 사례 포도주 끝까지 다마심
    if idx == n:
        return grape[n]
    # 기저 사례 포도주 개수 범위 밖
    if idx > n:
        return 0

    if cache[can][idx] != -1:
        return cache[can][idx]

    cache[can][idx] = grape[idx]

    if can <= 1:
        cache[can][idx] = max(cache[can][idx] + drink(can + 1, idx + 1), # 연속으로 마심
                              cache[can][idx] + drink(1, idx + 2),       # 한 잔을 건너뜀
                              cache[can][idx] + drink(1, idx + 3)        # 두 잔을 건너뜀
                              )                                          # 세잔을 건너뛰는건 없음 oxxxo < oxoxo 임
    elif can == 2:
        cache[can][idx] = max(cache[can][idx] + drink(1, idx + 2),       # 한 잔을 건너뜀
                              cache[can][idx] + drink(1, idx + 3))       # 두 잔을 건너뜀

    return cache[can][idx]

print(drink(0, 0))
