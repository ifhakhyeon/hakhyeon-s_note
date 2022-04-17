import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
pack = list(map(int, input().split()))
cache = [-1] * (n+1)
def dnf(card, buy):
    if buy == n:
        return 0
    if buy > n or card >= n:
        return -9876543210
    if cache[buy] != -1:
        return cache[buy]
    # 난 여기서 card번째 카드를 고르고 또 그카드를 고를 가능성이 있다.
    # card 번째 카드를 고르고 그 다음카드를 고른다.
    # card 번째 카드를 고르지 않는다.
    # 이렇게 세 경우의 수로 나눠서 ac를 받았지만 다시봐도 영 코드가 난잡하다.
    # 게다가 재귀를 너무 많이한다.
    ret = max(dnf(card, buy+card+1) + pack[card], dnf(card+1, buy+card+1) + pack[card], dnf(card+1, buy))
    cache[buy] = ret

    return ret

print(dnf(0, 0))

# 반면 다음 코드를 보자
"""
작은 문제부터 생각해본다. 카드를 한개 사는법부터
dp[i] = 카드 i개 구매하는 최대 가격 , p[k] = k개가 들어있는 카드팩 가격 이라고 했을때
카드를 i개 구매하는 최대 비용은 다음과 같다.
p[1] + dp[i-1]
p[2] + dp[i-2]
p[3] + dp[i-3]
    '
    '
p[i] + dp[0]
따라서 점화식은 dp[i] = p[k] + dp[i - k] 가 된다.
"""
N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])

print(dp[N])

# 다보고 11057도 다시보자
