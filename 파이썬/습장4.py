import sys
input = sys.stdin.readline

n, K = map(int, input().split())
numlist = list(map(int, input().split()))
for i in range(1, n):
    numlist[i] += numlist[i-1]
# print(numlist)
numlist.append(0)
p1 = 0
p2 = 0
ans = n+1
while p1 <= n-1 and p2 <= n-1:

    if numlist[p2] - numlist[p1-1] < K:
        p2 += 1
    elif numlist[p2] - numlist[p1-1] >= K:
        # print(p1, p2, numlist[p2] - numlist[p1-1])
        ans = min(ans, p2-p1+1)
        p1 += 1
print(ans if ans != n+1 else 0)