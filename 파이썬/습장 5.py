import sys
import math
# import time
# import datetime

input = sys.stdin.readline
N = int(input())
poly = list(map(int, input().split()))
# start = time.time()
if N == 0:
    print(f'GGG<{poly[0]}>')
    exit(0)

mod = (10**9) + 7
cache = [-1]*(N+1)

def comb(n, m):
    up = math.factorial(n)
    down = (math.factorial(n - m)) * (math.factorial(m))
    return (up // down) % mod

def cal(arr: list, x: int) -> int:
    # print(arr, x)
    if x == 0:
        return arr[0]
    if x == 1:
        return sum(arr) % mod
    ret = 0
    for i in range(len(arr)):
        ret += arr[i]*(x**i)
    return ret % mod

for i in range(N+1):
    cache[i] = cal(poly, i)

ans = [poly[0]]

for i in range(1, N+1):
    m = 0
    for j in range(i):
        m += (cache[j+1] * comb(i-1, j) * ((-1)**(i-j-1)))
    m %= mod
    m = ((m - ans[-1])+mod) % mod
    ans.append(m)
    # print(ans)
# print(ans)
a = ','.join(map(str, ans))
print(f'GGG<{a}>')
# end = time.time()
# sec = (end - start)
# result = datetime.timedelta(seconds=sec)
# print(result)