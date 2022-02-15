C = int(input())

for _ in range(C):
    deep, day = map(int, input().split())
    cache = [[-1 for _ in range(1001)] for _ in range(100000)]
    def clime(days, climed):
        if days == day:
            if climed >= deep:
                return 1
            else:
                return 0
        if cache[days][climed] != -1:
            return cache[days][climed]
        cache[days][climed] = 0.25 * clime(days+1, climed+1) + 0.75 * clime(days+1, climed+2)
        return cache[days][climed]

    print(clime(0, 0))