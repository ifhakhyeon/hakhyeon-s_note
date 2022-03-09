import sys
import heapq                    # 최대 힙
from queue import PriorityQueue # 우선순위 큐
input = sys.stdin.readline


C = int(input())
for _ in range(C):
    n = int(input())
    numlst = list(map(int, input().split()))
    ans = 0
    q = []
    for i in numlst:
        heapq.heappush(q, i)
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += a + b
        heapq.heappush(q, a + b)
    print(ans)


C = int(input())
for _ in range(C):
    que = PriorityQueue()
    n = int(input())
    numlist = list(map(int, input().split()))
    for i in numlist:
        que.put(i)
    ans = 0
    for _ in range(n-1):
        a = que.get()
        b = que.get()
        ans += (a+b)
        que.put(a+b)
    print(ans)