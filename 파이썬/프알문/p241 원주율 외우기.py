import sys
input = sys.stdin.readline

inf = 987654321
C = int(input())
for _ in range(C):
    pi = input()
    cache = [-1 for _ in range(pi+1)]
    def classify(start, end):
        subpi = pi[start: end+1]

        if subpi == subpi[0] * len(subpi):
            return 1

        seq = True
        for i in range(0, len(subpi)-1):
            if int(subpi[i]) - int(subpi[i+1]) != int(subpi[0]) - int(subpi[1]):
                seq = False
                break
        if seq and abs(int(subpi[0]) - int(subpi[1])) == 1:
            return 2

        alternately = True
        for i in range(0, len(subpi)):
            if subpi[i] != subpi[i % 2]:
                alternately = False
                break
        if alternately:
            return 4
        if seq:
            return 5
        return 10

    def solve(begin):
        if begin == len(pi)-1:
            return 0

        if cache[begin] != -1:
            return cache[begin]

        cache[begin] = inf
        for i in range(3, 6):
            if begin + i < len(pi):
                cache[begin] = min(cache[begin], solve(begin+i) + classify(begin, begin+i-1))

        return cache[begin]

    print(solve(0))