import sys
input = sys.stdin.readline

N, K = map(int, input().split())
backpack = []
cache = [[-1 for _ in range(N+1)] for _ in range(K+1)]

# weight 는 남은 용량, item은 인덱스를 넣는다.
def peek(weight, item):
    # 기저 사례 물건이 꽉참 공간이 꽉안차도 만족도가 최대일 수 있음
    if item == N:
        return 0
    if cache[weight][item] != -1:
        return cache[weight][item]
    # 물건을 담지 않음
    cache[weight][item] = peek(weight, item + 1)
    # 물건을 담음
    if (weight >= backpack[item][0]):
        cache[weight][item] = max(cache[weight][item],
                                  peek(weight - backpack[item][0], item + 1) + backpack[item][1]
                                  )
    return cache[weight][item]


for _ in range(N):
    a = tuple(map(int, input().split()))
    backpack.append(a)

print(peek(K, 0))

