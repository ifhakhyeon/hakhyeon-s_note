import sys
input = sys.stdin.readline
import math

N = int(input())
numlist = []
numlist.append(int(input()))
numlist.append(int(input()))
g = abs(numlist[-1] - numlist[-2])

for _ in range(N-2):
    numlist.append(int(input()))
    g = math.gcd(g, abs(numlist[-1] - numlist[-2]))

ans = []
if g == 0:
    g = numlist[-1]
maxn = int(g**(1/2))

for i in range(2, maxn + 1):
    if g % i == 0:
        ans.append(i)
        ans.append(g//2)

ans.append(g)
ans = list(set(ans))
ans.sort()

for i in ans:
    print(i, end=' ')
