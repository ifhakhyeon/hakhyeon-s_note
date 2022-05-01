import sys
from queue import PriorityQueue
import heapq
input = sys.stdin.readline

# 1
n = int(input())
_class = [tuple(map(int, input().split())) for _ in range(n)]
_class.sort()

a = PriorityQueue()
a.put(_class[0][1])
for i in range(1, n):
    k = a.get()
    # print(k)
    if k > _class[i][0]:
        a.put(k)
        a.put(_class[i][1])
    else:
        a.put(_class[i][1])
print(a.qsize())

# 2
n = int(input())
_class = [tuple(map(int, input().split())) for _ in range(n)]
_class.sort()

a = []
heapq.heappush(a, _class[0][1])
for i in range(1, n):
    k = heapq.heappop(a)
    # print(k)
    if k > _class[i][0]:
        heapq.heappush(a, k)
        heapq.heappush(a, _class[i][1])
    else:
        heapq.heappush(a, _class[i][1])
print(len(a))