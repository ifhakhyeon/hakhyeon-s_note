C = int(input())
cache = [-1 for _ in range(101)]
for _ in range(C):
    n = int(input())
    def tiling(n):
        # n == 2 일 때 tiling(0) 이 호출 되는데 tiling(2) 는 자명히 2이다
        # 그러므로 tiling(0)도 1이다.
        if n <= 1:
            return 1

        if cache[n] != -1:
            return cache[n]
        cache[n] = (tiling(n-1) + tiling(n-2)) % 1000000007
        return cache[n]

    print(tiling(n))

