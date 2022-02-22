import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

cache = {1: 0, 2: 1}
n = int(input())

def count(num):
    if num in cache:
        return cache[num]

    # 와 씨발 이거 개 천재인듯;;
    cnt = 1 + min(count(num//3) + num % 3,
                  count(num//2) + num % 2)

    cache[num] = cnt

    return cache[num]

print(count(n))