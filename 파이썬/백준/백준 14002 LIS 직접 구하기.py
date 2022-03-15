import sys
input = sys.stdin.readline

def lis(arr):
    if not arr:
        return 0
    tmp_longest = 1
    INF = float('inf')
    cache = [INF] * (len(S) + 1)
    cache[0] = -INF
    cache[1] = S[0]
    # Find i that matches C[i-1] < num <= C[i]
    def search(lo, hi, num):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if cache[lo] >= num else hi

        mid = (lo + hi) // 2
        if cache[mid] == num:
            return mid
        elif cache[mid] < num:
            return search(mid + 1, hi, num)
        else:
            return search(lo, mid, num)

    for i in arr:
        if cache[tmp_longest] < i:
            tmp_longest += 1
            cache[tmp_longest] = i
        else:
            next_loc = search(0, tmp_longest, i)
            cache[next_loc] = i

    return tmp_longest

n = int(input())
S = list(map(int, input().split()))

dp = [-1 for _ in range(n+1)]
choice = [-1 for _ in range(n+1)]
def find(start):
    ret = dp[start]
    if ret != -1:
        return ret
    ret = 1
    bestNext = -1
    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            cand = find(next) + 1
            if cand > ret:
                ret = cand
                bestNext = next
    dp[start] = ret
    choice[start+1] = bestNext
    return ret

seq = []
def reconstruct(start, seq):
    if start != -1:
        seq.append(S[start])
    next = choice[start+1]
    if next != -1:
        reconstruct(next, seq)

find(-1)
maxlis = dp[-1] - 1
start = dp.index(maxlis)
reconstruct(start, seq)
print(maxlis)
for i in seq:
    print(i, end=' ')