import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewelryList = []
for _ in range(N):
    jewelryList.append(tuple(map(int, input().split())))

bagList = []
for _ in range(K):
    bagList.append(int(input()))

jewelryList.sort()
bagList.sort()

ans = 0
temp = []

for bagWeight in bagList:
    while jewelryList and bagWeight >= jewelryList[0][0]:
        # 최대힙 즉 heapq.heappop 을 하면 최대값(최대 보석가치) 를 반환해야함
        heapq.heappush(temp, -jewelryList[0][1])
        heapq.heappop(jewelryList)
        # print(jewelryList)

    if temp:
        ans += heapq.heappop(temp)
    elif not jewelryList:
        break

print(-ans)