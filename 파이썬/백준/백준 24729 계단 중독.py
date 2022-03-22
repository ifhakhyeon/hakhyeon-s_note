import sys
input = sys.stdin.readline
_=input()
numlist = list(map(int, input().split()))
if len(numlist) % 2 == 1:
    print(-1)
    exit(0)

m = min(numlist)
n = max(numlist)

a = [0 for _ in range(m, n + 1)]
for i in numlist:
    a[i - m] += 1

ans = True
ret = a[0]
for i in range(0, n - m):
    if ret <= 0:
        ans = False
        break
    else:
        ret = a[i+1] - ret

if ret == 0 and ans:
    print(1)
else:
    print(-1)