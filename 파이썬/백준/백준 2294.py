import sys
import math
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin = list(set(coin))
coin.sort()
n = len(coin)
cache = [-1] * (k + 1)
# m 은 지금까지 코인의 가지
# i 는 coin에서의 인덱스 lec(coin)-1까지
def c(m, i):
    # 가격이 더 크거나 인덱스가 더 커지면 큰 수 return
    if m > k or i >= n:
        return 9876543210
    # 가격이 맞으면 0 return
    if m == k:
        return 0
    if cache[m] != -1:
        return cache[m]
    # 지금위치의 코인을 고르고 (고른만큼 가격 +) 계속 지금위치에 머물거나
    # 지금위치의 코인을 고르고 다음위치로 이동하거나
    # 지금위치의 코인을 고르지 않고 다음위치로 이동하거나
    # 중의 최솟값
    ret = min(c(m + coin[i], i) + 1, c(m + coin[i], i + 1) + 1, c(m, i + 1))

    # cache는 지금 가격이 m 일 때의 고르는 코인의 최소값임
    cache[m] = ret

    return ret

ans = c(0, 0)
if ans > k:
    print(-1)
else:
    print(ans)

# ver2
input = sys.stdin.readline
INF = math.inf
n, k = map(int, input().split())
coin = []
cache = [INF for i in range(k + 1)]

for i in range(n):
    coin.append(int(input()))

for i in coin:
    if i > k:
        continue
    cache[i] = 1
    for j in range(i + 1, k + 1):
        if j != i:
            if cache[j - i] != INF:
                cache[j] = min(cache[j - i] + 1, cache[j])


print(cache[k] if cache[k] != INF else -1)