import sys

input = sys.stdin.readline


def lis(arr):
    if not arr:
        return 0

    INF = float('inf')
    cache = [-INF] * (len(arr) + 1)
    cache[0] = INF
    cache[1] = arr[0]
    tmp_longest = 1

    def search(lo, hi, num):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if cache[lo] <= num else hi

        mid = (lo + hi) // 2
        if cache[mid] == num:
            return mid
        elif cache[mid] > num:
            return search(mid + 1, hi, num)
        else:
            return search(lo, mid, num)

    for i in arr:
        if cache[tmp_longest] > i:
            tmp_longest += 1
            cache[tmp_longest] = i
        else:
            next_loc = search(0, tmp_longest, i)
            cache[next_loc] = i

    return tmp_longest


n = int(input())
S = list(map(int, input().split()))
print(lis(S))