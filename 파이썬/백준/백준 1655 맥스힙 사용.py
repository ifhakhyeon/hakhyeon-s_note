import sys
import heapq
input = sys.stdin.readline

n = int(input())
left = []
righ = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(left) == len(righ):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(righ, num)

    if righ and righ[0] < -left[0]:
        leftValue = heapq.heappop(left)
        rightValue = heapq.heappop(righ)

        heapq.heappush(left, -rightValue)
        heapq.heappush(righ, -leftValue)

    print(-left[0])


