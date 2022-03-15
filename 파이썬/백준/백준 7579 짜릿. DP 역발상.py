import sys
input = sys.stdin.readline

N, M = map(int, input().split())
byte = list(map(int, input().split()))
all_byte = sum(byte)
c = list(map(int, input().split()))
all_cost = sum(c)
# cache[현제 idx][cost]
cache = [[-1 for _ in range(N)] for _ in range(N * 100 + 1)]
def peek(idx, cost):
    if idx == N:
        return 0

    if cache[cost][idx] != -1:
        return cache[cost][idx]

    ret = peek(idx + 1, cost)
    if cost >= c[idx]:
        ret = max(ret,
                  peek(idx + 1, cost - c[idx]) + byte[idx])
    cache[cost][idx] = ret
    return ret
# 중요한건 cost 가 주어질 때 가장 많이 끌 수 있는 app byte를 찾는것 이였다.
for i in range(N * 100 + 1):
    if peek(0, i) >= M:
        print(i)
        break