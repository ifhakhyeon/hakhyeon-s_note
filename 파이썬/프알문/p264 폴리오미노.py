mod = 1000*1000*10
cache = [[-1 for _ in range(101)] for _ in range(101)]

def poly(n, first):
    if n == first:
        return 1
    if cache[n][first] != -1:
        return cache[n][first]
    cache[n][first] = 0
    for second in range(1, n-first+1):
        add = second + first-1
        add *= poly(n-first, second)
        add %= mod
        cache[n][first] += add
        cache[n][first] %= mod

    return cache[n][first]

C = int(input())
for _ in range(C):
    n = int(input())
    ret = 0
    for i in range(1, n+1):
        ret += poly(n, i)
    print(ret % mod)