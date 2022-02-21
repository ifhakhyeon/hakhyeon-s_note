import sys
input = sys.stdin.readline

n = int(input())
mod = 1000*1000*1000
cache = [[-1 for _ in range(10)] for _ in range(n)]
num = [-1 for _ in range(n)]

def stairnum(idx, num):
    if idx == 0 and num == 0:
        return 0
    if idx == n-1:
        return 1

    if cache[idx][num] != -1:
        return cache[idx][num]

    cache[idx][num] = 0

    if 1 <= num <= 8:
        cache[idx][num] = ((cache[idx][num] % mod) +
                           (stairnum(idx+1, num+1) % mod) +
                           (stairnum(idx+1, num-1) % mod)) % mod
    elif num == 0:
        cache[idx][num] = ((cache[idx][num] % mod) + (stairnum(idx+1, num+1) % mod)) % mod
    elif num == 9:
        cache[idx][num] = (cache[idx][num] % mod + (stairnum(idx + 1, num - 1) % mod)) % mod

    return cache[idx][num] % mod

ret = 0

for i in range(1,10):
    ret += stairnum(0, i)
    ret %= mod
print(ret)