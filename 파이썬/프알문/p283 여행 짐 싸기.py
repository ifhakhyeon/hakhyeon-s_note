import sys
import copy
input = sys.stdin.readline

C = int(input())
thingsdic = {}
thingslist = []
# capacity 는 남은 용량, item은 아이템의 인덱스를 넣는다.
def peek(capactiy, item):
    # 기저 사례 물건이 꽉참 공간이 꽉안차도 만족도가 최대일 수 있음
    if item == N:
        return 0
    if cache[capactiy][item] != -1:
        return cache[capactiy][item]
    # 물건을 담지 않음
    cache[capactiy][item] = peek(capactiy, item+1)
    # 물건을 담음
    if (capactiy >= thingsdic[thingslist[item]][0]):
        cache[capactiy][item] = max(cache[capactiy][item],
                                    peek(capactiy-thingsdic[thingslist[item]][0], item+1)+thingsdic[thingslist[item]][1]
                                    )
    return cache[capactiy][item]

def refind(capactiy, item, picked):
    if item == N:
        return
    if peek(capactiy, item) == peek(capactiy, item+1):
        refind(capactiy, item+1, picked)
    else:
        picked.append(thingslist[item])
        refind(capactiy-thingsdic[thingslist[item]][0], item+1, picked)
    return picked

for _ in range(C):
    cache = [[-1 for _ in range(101)] for _ in range(101)]
    N, W = map(int, input().split())
    for _ in range(N):
        a, b, c = input().split()
        thingsdic[a] = int(b), int(c)
        thingslist.append(a)
    ret = refind(W, 0, [])
    print(peek(W, 0), len(ret))
    for i in ret:
        print(i)

# 동적 계획법 너무 어려워요 싸장님..