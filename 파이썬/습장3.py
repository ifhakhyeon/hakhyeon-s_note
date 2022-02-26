import math

N = int(input())
numlist = []
ans = []
gcd = 0

for i in range(N):
    numlist.append(int(input()))
    if i == 1:
        gcd = abs(numlist[1] - numlist[0])
    gcd = math.gcd(abs(numlist[i] - numlist[i - 1]), gcd)

maxn = int(gcd ** (1 / 2))
for i in range(2, maxn + 1):
    if gcd % i==0:
        ans.append(i)
        ans.append(gcd // i)

ans.append(gcd)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i, end=' ')