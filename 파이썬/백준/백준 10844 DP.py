import sys
input = sys.stdin.readline

cache = [[-1 for _ in range(301)] for _ in range(3)]

n = int(input())
stair_score = [0]
for _ in range(n):
    stair_score.append(int(input()))

def score(can, idx):
    # 기저 사례 계단 끝에 도착
    if idx == n:
        return stair_score[n]
    # 기저 사례 계단 끝을 못밟음
    if idx > n:
        return -9876543210

    if cache[can][idx] != -1:
        return cache[can][idx]

    cache[can][idx] = stair_score[idx]

    if can <= 1:
        cache[can][idx] = max(cache[can][idx] + score(can+1, idx+1), cache[can][idx] + score(1, idx+2))
    elif can == 2:
        cache[can][idx] = cache[can][idx] + score(1, idx+2)

    return cache[can][idx]

print(score(0, 0))
