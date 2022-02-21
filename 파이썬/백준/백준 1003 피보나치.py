C = int(input())

cache = [[-1, -1] for _ in range(41)]

def fib(N):
    if N == 0:
        return 1, 0
    if N == 1:
        return 0, 1
    if cache[N][0] != -1 and cache[N][1] != -1:
        return cache[N][0], cache[N][1]

    cache[N][0], cache[N][1] = 0, 0
    cache[N][0], cache[N][1] = cache[N][0] + fib(N-1)[0] + fib(N-2)[0], cache[N][1] + fib(N-1)[1] + fib(N-2)[1]

    return cache[N]

for _ in range(C):
    N = int(input())
    a, b = fib(N)
    print(a, b)